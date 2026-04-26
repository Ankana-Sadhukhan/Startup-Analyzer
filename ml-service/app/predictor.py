from .innovation import get_innovation_score
from .swot import generate_swot_analysis, generate_metrics_breakdown, generate_pitch_outline
from .explainability import generate_explanation, get_innovation_breakdown, generate_success_factors
from .competitor_mapping import (
    generate_competitor_analysis,
    get_competitive_advantages,
    get_market_entry_strategy
)

def predict_idea(idea):
    innovation_data = get_innovation_score(idea)
    innovation_score = float(innovation_data["innovation_score"])
    cleaned_idea = innovation_data["cleaned_idea"]
    max_similarity = float(innovation_data["max_similarity"])
    interpretation = innovation_data["interpretation"]
    top_similar_ideas = innovation_data["top_similar_ideas"]
    
    # Convert numpy floats to Python floats in top_similar_ideas
    for item in top_similar_ideas:
        item["similarity"] = float(item["similarity"])
    
    # Generate SWOT analysis
    swot_analysis = generate_swot_analysis(idea, innovation_score, max_similarity, interpretation)
    
    # Generate detailed metrics for visualizations
    metrics_breakdown = generate_metrics_breakdown(innovation_score, max_similarity)
    
    # Generate pitch deck outline
    pitch_outline = generate_pitch_outline(idea, innovation_score, interpretation, swot_analysis)
    
    # Generate XAI explanations
    explanations = generate_explanation(idea, innovation_score, max_similarity, top_similar_ideas, metrics_breakdown)
    innovation_breakdown = get_innovation_breakdown(innovation_score)
    success_factors = generate_success_factors(idea, metrics_breakdown)
    
    # Generate competitor analysis
    competitor_analysis = generate_competitor_analysis(idea, top_similar_ideas)
    competitive_advantages = get_competitive_advantages(swot_analysis, metrics_breakdown)
    market_entry_strategy = get_market_entry_strategy(innovation_score, metrics_breakdown)
    
    return {
        "idea": idea,
        "cleaned_idea": cleaned_idea,
        "max_similarity": max_similarity,
        "innovation_score": innovation_score,
        "interpretation": interpretation,
        "top_similar_ideas": top_similar_ideas,
        "swot": swot_analysis,
        "metrics": metrics_breakdown,
        "pitch_deck": pitch_outline,
        "explanation": explanations,
        "innovation_breakdown": innovation_breakdown,
        "success_factors": success_factors,
        "competitors": competitor_analysis,
        "competitive_advantages": competitive_advantages,
        "market_strategy": market_entry_strategy
    }