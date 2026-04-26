import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

### 8.3. NLP-based Innovation Score System

# This section implements a new, self-contained system to calculate an innovation score for a given startup idea.
# It uses sentence embeddings and cosine similarity to compare the input idea against a predefined list of common startup ideas.
# The core idea is that the less semantically similar an idea is to existing common ideas, the higher its innovation score.

# 1. Existing Ideas: List of common startup ideas (expanded to meet 50-100 requirement)
common_startup_ideas = [
    "Food delivery app", "E-commerce platform for handmade goods", "Ride-sharing service",
    "Online tutoring platform", "Social media marketing agency", "Subscription box for pet supplies",
    "AI-powered chatbot for customer service", "Fintech app for personal budgeting",
    "Healthcare telemedicine platform", "Edtech platform for coding bootcamps",
    "Local bakery delivery service", "Smart home security system", "Sustainable fashion brand",
    "Cloud-based project management software", "Mobile game development studio",
    "Virtual reality fitness app", "Personalized nutrition plan service", "Co-working space for freelancers",
    "Online marketplace for local services", "Podcast production company", "Digital marketing consulting",
    "SaaS for small business CRM", "Online course platform", "Cybersecurity solutions for SMEs",
    "Meal kit delivery service", "Blockchain supply chain tracking", "Renewable energy consulting",
    "On-demand car wash service", "Pet-sitting and dog walking app", "Custom jewelry e-commerce",
    "DIY craft kit subscription", "Plant-based meal delivery", "Senior care technology",
    "Gamified education app for kids", "Voice-controlled smart assistant", "Rental marketplace for tools",
    "Personal finance advisory service", "Smart garden system", "Augmented reality shopping app",
    "Waste management and recycling solutions", "Online art gallery", "Event planning software",
    "Virtual event platform", "Sustainable packaging solutions", "Personalized travel planning",
    "Mental wellness app with AI coach", "Drone-based inspection services", "Smart farming solutions",
    "Online community for remote workers",
    "AR-powered navigation for museums", "Bio-tech solutions for sustainable agriculture",
    "Quantum computing as a service", "Decentralized identity management", "AI for personalized medicine",
    "Vertical farming automation", "Wearable tech for elder care", "Robotics for hazardous environment inspection",
    "Space tourism booking platform", "Neural interface for disability assistance",
    "Predictive analytics for urban planning", "Self-driving car software", "Ocean plastic cleanup technology",
    "Sustainable fashion upcycling platform", "Hyperloop transportation systems",
    "Personalized genomic diet plans", "AI-driven drug discovery", "Automated legal contract generation",
    "VR training simulations for surgery", "Digital twin technology for manufacturing",
    "Climate change impact modeling", "Smart city infrastructure development", "Renewable energy grid optimization",
    "AI-powered mental health chatbot for teens", "Edtech platform for vocational skills",
    "Blockchain for real estate transactions", "Customizable prosthetic limbs with AI",
    "Advanced material science for construction", "Water purification using nanotechnology",
    "Ethical AI development consulting", "Smart recycling bins with AI sorting",
    "Precision agriculture with IoT sensors", "Robotic baristas for cafes", "Generative AI for artistic creation",
    "Personalized education paths using adaptive learning", "Gamified fitness challenges with blockchain rewards",
    "AI-driven fraud detection for fintech", "Virtual reality therapy for phobias",
    "Sustainable packaging from mushroom mycelium", "Personalized news aggregation with AI curation",
    "Smart home devices for energy efficiency", "Predictive maintenance for industrial machinery",
    "Edtech platform for neurodiverse learners", "AI for personalized legal advice",
    "Blockchain-based carbon credit trading", "Reusable packaging delivery system",
    "AI-powered content moderation for social media", "Bio-luminescent street lighting"
]

# 2. Text Preprocessing Function
def preprocess_text(text: str) -> str:
    """
    Converts text to lowercase and removes common generic words.
    """
    text = text.lower()
    # Define common generic words to remove
    generic_words = ["app", "platform", "system", "solution", "online", "service", "startup", "idea"]
    # Create a regex pattern to match whole words
    pattern = r'\b(?:' + '|'.join(generic_words) + r')\b'
    text = re.sub(pattern, '', text)
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra spaces
    return text

# 3. Load pre-trained Sentence Transformer model
# This model converts sentences/phrases into numerical vectors (embeddings)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Preprocess and embed all common startup ideas once
cleaned_common_ideas = [preprocess_text(idea) for idea in common_startup_ideas]
common_idea_embeddings = embedding_model.encode(cleaned_common_ideas, show_progress_bar=False)

def get_innovation_score(idea: str) -> dict:
    """
    Calculates an innovation score (0-10) for a given startup idea using sentence embeddings.
    Lower semantic similarity to existing ideas implies higher innovation.

    Args:
        idea (str): The startup idea to analyze.

    Returns:
        dict: A structured result containing the idea, cleaned idea, max similarity,
              innovation score, interpretation, and top similar ideas.
    """
    print("\nThis score is based on semantic similarity using embeddings. Lower similarity indicates higher innovation.")

    # Preprocess the input idea
    cleaned_idea = preprocess_text(idea)

    # Convert the cleaned input idea into an embedding
    idea_embedding = embedding_model.encode([cleaned_idea], show_progress_bar=False)[0]

    # Calculate cosine similarity between the input idea's embedding and all common idea embeddings
    similarities = cosine_similarity([idea_embedding], common_idea_embeddings)[0]

    # Find the maximum similarity score and its index
    max_similarity = similarities.max()
    max_similarity_idx = similarities.argmax()

    # Compute Innovation Score: (1 - max_similarity) * 10
    innovation_score = round((1 - max_similarity) * 10, 2)
    innovation_score = max(0.0, min(10.0, innovation_score)) # Clamp between 0 and 10

    # Determine interpretation (Improved Logic)
    if innovation_score < 4:
        interpretation = "Low Innovation (common idea)"
    elif 4 <= innovation_score <= 7:
        interpretation = "Moderate Innovation"
    else:
        interpretation = "Highly Innovative Idea"

    # Debug/Visibility: Find top 3 most similar ideas
    top_3_indices = similarities.argsort()[-3:][::-1] # Get indices of top 3 similarities, in descending order
    top_3_similar_ideas = []
    for i in top_3_indices:
        top_3_similar_ideas.append({
            "idea": common_startup_ideas[i],
            "similarity": round(similarities[i], 2)
        })

    # Print top 3 similar ideas for debugging
    print("  Top 3 most similar existing ideas:")
    for item in top_3_similar_ideas:
        print(f"    - '{item['idea']}' (Similarity: {item['similarity']})")

    return {
        "idea": idea,
        "cleaned_idea": cleaned_idea,
        "max_similarity": round(max_similarity, 2),
        "innovation_score": innovation_score,
        "interpretation": interpretation,
        "top_similar_ideas": top_3_similar_ideas
    }
