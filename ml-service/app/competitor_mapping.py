"""
Competitor Mapping and Market Intelligence Generator
Provides competitor analysis and market positioning insights.
"""

# Map of common startup keywords to potential competitors
COMPETITOR_DATABASE = {
    "ecommerce": [
        {"name": "Shopify", "type": "Platform", "market_share": "High", "founded": 2006},
        {"name": "Amazon Business", "type": "Marketplace", "market_share": "Very High", "founded": 1994},
        {"name": "WooCommerce", "type": "Plugin", "market_share": "High", "founded": 2011},
    ],
    "saas": [
        {"name": "Salesforce", "type": "CRM", "market_share": "Very High", "founded": 1999},
        {"name": "Microsoft 365", "type": "Productivity", "market_share": "Very High", "founded": 1985},
        {"name": "Slack", "type": "Communication", "market_share": "High", "founded": 2013},
    ],
    "ai": [
        {"name": "OpenAI", "type": "AI Platform", "market_share": "Very High", "founded": 2015},
        {"name": "Google AI", "type": "AI Services", "market_share": "Very High", "founded": 1998},
        {"name": "Hugging Face", "type": "AI Models", "market_share": "Medium", "founded": 2016},
    ],
    "fintech": [
        {"name": "Stripe", "type": "Payments", "market_share": "Very High", "founded": 2010},
        {"name": "PayPal", "type": "Payments", "market_share": "Very High", "founded": 1998},
        {"name": "Square", "type": "Payments", "market_share": "High", "founded": 2009},
    ],
    "logistics": [
        {"name": "FedEx", "type": "Delivery", "market_share": "Very High", "founded": 1971},
        {"name": "Amazon Logistics", "type": "Delivery", "market_share": "Very High", "founded": 2014},
        {"name": "Uber Freight", "type": "Logistics", "market_share": "High", "founded": 2016},
    ],
    "healthcare": [
        {"name": "Teladoc", "type": "Telehealth", "market_share": "High", "founded": 2002},
        {"name": "Ro", "type": "Telehealth", "market_share": "Medium", "founded": 2017},
        {"name": "Amazon Pharmacy", "type": "Pharmacy", "market_share": "Growing", "founded": 2020},
    ],
    "education": [
        {"name": "Coursera", "type": "Online Learning", "market_share": "High", "founded": 2012},
        {"name": "Udemy", "type": "Online Learning", "market_share": "High", "founded": 2010},
        {"name": "LinkedIn Learning", "type": "Professional Dev", "market_share": "High", "founded": 2015},
    ],
    "social": [
        {"name": "Meta", "type": "Social Network", "market_share": "Very High", "founded": 2004},
        {"name": "TikTok", "type": "Video Platform", "market_share": "Very High", "founded": 2016},
        {"name": "Discord", "type": "Community", "market_share": "High", "founded": 2015},
    ],
}

def generate_competitor_analysis(idea: str, top_similar_ideas: list) -> dict:
    """
    Generate competitor analysis based on the startup idea.
    
    Args:
        idea (str): The startup idea
        top_similar_ideas (list): Top similar existing ideas from market analysis
    
    Returns:
        dict: Competitor analysis with direct and indirect competitors
    """
    
    idea_lower = idea.lower()
    
    direct_competitors = []
    indirect_competitors = []
    adjacents = []
    
    # Find relevant competitors from database
    for category, competitors in COMPETITOR_DATABASE.items():
        if category.lower() in idea_lower or idea_lower in category.lower():
            direct_competitors.extend(competitors[:2])  # Top 2 from each category
        else:
            # These could be indirect competitors or adjacent markets
            indirect_competitors.extend(competitors[:1])
    
    # Parse top similar ideas to add as direct competitors
    for similar_idea in top_similar_ideas[:3]:
        direct_competitors.append({
            "name": similar_idea["idea"],
            "type": "Market Alternative",
            "market_share": "Medium",
            "founded": "Unknown"
        })
    
    # Identify adjacent market opportunities
    adjacents = _find_adjacent_markets(idea_lower)
    
    return {
        "direct_competitors": direct_competitors[:5],  # Top 5 direct
        "indirect_competitors": indirect_competitors[:3],  # Top 3 indirect
        "adjacent_markets": adjacents,
        "competitive_landscape_summary": _generate_landscape_summary(
            len(direct_competitors),
            len(indirect_competitors)
        )
    }


def _find_adjacent_markets(idea_lower: str) -> list:
    """
    Identify adjacent market opportunities based on the idea.
    
    Args:
        idea_lower (str): Lowercase idea string
    
    Returns:
        list: Adjacent market opportunities
    """
    
    adjacents = []
    
    # Technology adjacencies
    if any(word in idea_lower for word in ['mobile', 'app', 'web']):
        adjacents.append({
            "market": "Cross-platform expansion",
            "opportunity": "Expand from Web to Mobile or vice versa",
            "difficulty": "Medium"
        })
    
    if any(word in idea_lower for word in ['b2c', 'consumer', 'retail']):
        adjacents.append({
            "market": "B2B Enterprise market",
            "opportunity": "Create enterprise/B2B version",
            "difficulty": "High"
        })
    elif any(word in idea_lower for word in ['b2b', 'enterprise', 'saas']):
        adjacents.append({
            "market": "Consumer/B2C market",
            "opportunity": "Create consumer version",
            "difficulty": "Medium"
        })
    
    if any(word in idea_lower for word in ['us', 'north america', 'english']):
        adjacents.append({
            "market": "International expansion",
            "opportunity": "Expand to European, Asian markets",
            "difficulty": "High"
        })
    
    # Vertical integration opportunities
    adjacents.append({
        "market": "Vertical integration",
        "opportunity": "Integrate complementary services",
        "difficulty": "High"
    })
    
    # Marketplace/Platform opportunities
    if not any(word in idea_lower for word in ['marketplace', 'platform']):
        adjacents.append({
            "market": "Ecosystem/Platform play",
            "opportunity": "Build ecosystem around core offering",
            "difficulty": "Very High"
        })
    
    return adjacents[:4]


def _generate_landscape_summary(direct_count: int, indirect_count: int) -> str:
    """
    Generate a summary of the competitive landscape.
    
    Args:
        direct_count (int): Number of direct competitors found
        indirect_count (int): Number of indirect competitors
    
    Returns:
        str: Summary text
    """
    
    if direct_count >= 5:
        return "Highly competitive market with multiple established players. Success requires strong differentiation."
    elif direct_count >= 3:
        return "Competitive market with several key players. Clear positioning and unique value proposition are critical."
    elif direct_count == 2:
        return "Moderate competition with some established players. Opportunity exists for differentiation."
    else:
        return "Limited direct competition indicates either a novel market or insufficient market awareness. Requires careful validation."


def get_competitive_advantages(swot: dict, metrics: dict) -> dict:
    """
    Identify potential competitive advantages from SWOT analysis and metrics.
    
    Args:
        swot (dict): SWOT analysis data
        metrics (dict): Metrics breakdown
    
    Returns:
        dict: Competitive advantages analysis
    """
    
    advantages = {
        "primary": [],
        "secondary": [],
        "defensibility": []
    }
    
    # Extract competitive advantages from strengths
    if swot["strengths"]:
        advantages["primary"] = swot["strengths"][:3]  # Top 3 strengths
        advantages["secondary"] = swot["strengths"][3:]  # Rest of strengths
    
    # Assess defensibility
    if metrics["differentiation"] >= 7:
        advantages["defensibility"].append("High differentiation protects against competition")
    
    if metrics["innovation"] >= 7:
        advantages["defensibility"].append("Novel approach difficult for competitors to replicate")
    
    if metrics["scalability"] >= 7:
        advantages["defensibility"].append("Superior scalability enables cost advantages")
    
    if metrics["technical_feasibility"] >= 7:
        advantages["defensibility"].append("Technical barrier to entry slows competitors")
    else:
        advantages["defensibility"].append("Low technical barriers mean faster competitive response - focus on execution")
    
    return advantages


def get_market_entry_strategy(innovation_score: float, metrics: dict) -> dict:
    """
    Generate a recommended market entry strategy based on metrics.
    
    Args:
        innovation_score (float): Innovation score (0-10)
        metrics (dict): Detailed metrics
    
    Returns:
        dict: Market entry strategy recommendations
    """
    
    strategy = {
        "approach": "",
        "rationale": "",
        "timeline": "",
        "key_milestones": [],
        "risks": [],
        "opportunities": []
    }
    
    # Determine entry strategy based on innovation and market demand
    if innovation_score >= 8 and metrics["market_demand"] >= 7:
        strategy["approach"] = "Fast-track aggressive expansion"
        strategy["rationale"] = "High innovation + strong demand = capture market quickly before copycat competitors"
        strategy["timeline"] = "6-12 months to MVP, 12-24 months to Series A"
        strategy["key_milestones"] = [
            "Month 3: MVP launch",
            "Month 6: Product-market fit validation",
            "Month 9: First customers/revenue",
            "Month 12: Series A fundraising"
        ]
        strategy["opportunities"] = [
            "First-mover advantage",
            "Premium positioning",
            "Attract top talent"
        ]
        strategy["risks"] = [
            "Market may not be ready",
            "Execution complexity",
            "Regulatory surprises"
        ]
    
    elif innovation_score >= 5 and metrics["market_demand"] >= 6:
        strategy["approach"] = "Customer discovery then scale"
        strategy["rationale"] = "Moderate innovation with decent demand - validate before scaling"
        strategy["timeline"] = "3-6 months research, 6-12 months MVP, 12-18 months growth"
        strategy["key_milestones"] = [
            "Month 2: Customer interviews & validation",
            "Month 6: MVP with early adopters",
            "Month 10: Expansion based on feedback",
            "Month 18: Sustainable growth"
        ]
        strategy["opportunities"] = [
            "Learn from market leaders",
            "Build with customer input",
            "Reduce execution risk"
        ]
        strategy["risks"] = [
            "Longer time to market",
            "Competitors may innovate faster",
            "Market may shift"
        ]
    
    else:
        strategy["approach"] = "Deep market validation + differentiation"
        strategy["rationale"] = "Crowded market or uncertain demand - focus on finding your unique angle"
        strategy["timeline"] = "6-9 months validation, 9-15 months MVP, 15+ months growth"
        strategy["key_milestones"] = [
            "Month 3: Deep market research complete",
            "Month 6: Differentiation strategy defined",
            "Month 12: MVP with strong differentiation",
            "Month 18: Customer acquisition strategy validated"
        ]
        strategy["opportunities"] = [
            "Avoid crowded positions",
            "Build stronger moat",
            "Better prepared for competition"
        ]
        strategy["risks"] = [
            "Very long runway needed",
            "Capital constraints",
            "Market may mature before launch"
        ]
    
    return strategy
