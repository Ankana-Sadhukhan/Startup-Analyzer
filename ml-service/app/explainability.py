"""
Explainable AI (XAI) Module
Provides detailed reasoning for innovation scores and analysis results.
This demonstrates AI transparency and interpretability for stakeholders.
"""

def generate_explanation(
    idea: str,
    innovation_score: float,
    max_similarity: float,
    top_similar_ideas: list,
    metrics: dict
) -> dict:
    """
    Generate detailed explanations for why the innovation score was assigned.
    
    Args:
        idea (str): The startup idea
        innovation_score (float): Innovation score (0-10)
        max_similarity (float): Max similarity to existing ideas (0-1)
        top_similar_ideas (list): Top 3 similar existing ideas
        metrics (dict): Detailed metrics breakdown
    
    Returns:
        dict: Detailed explanation with reasoning
    """
    
    explanations = {
        "innovation_reasoning": [],
        "market_analysis": [],
        "key_factors": [],
        "recommendations": [],
        "confidence_score": 0.0
    }
    
    # INNOVATION REASONING
    if innovation_score >= 8:
        explanations["innovation_reasoning"].append(
            "Your idea demonstrates HIGH INNOVATION - it differs significantly from existing market solutions."
        )
        explanations["innovation_reasoning"].append(
            f"Similarity to existing ideas: {max_similarity:.1%} (Low = Innovative)"
        )
        explanations["key_factors"].append("✓ Unique concept with minimal market precedent")
        explanations["key_factors"].append("✓ Potential to create entirely new market category")
        confidence = 0.92
        
    elif innovation_score >= 6:
        explanations["innovation_reasoning"].append(
            "Your idea shows MODERATE-TO-HIGH INNOVATION with some differentiation from existing solutions."
        )
        explanations["innovation_reasoning"].append(
            f"You have similarities to existing ideas ({max_similarity:.1%}), but offer unique angles."
        )
        explanations["key_factors"].append("✓ Clear differentiation from top competitors")
        explanations["key_factors"].append("✓ New value proposition in existing market")
        confidence = 0.88
        
    elif innovation_score >= 4:
        explanations["innovation_reasoning"].append(
            "Your idea shows MODERATE INNOVATION - it addresses real market needs but faces competition."
        )
        explanations["innovation_reasoning"].append(
            f"Market similarity: {max_similarity:.1%} indicates several existing competitors."
        )
        explanations["key_factors"].append("• Traditional market with room for improvement")
        explanations["key_factors"].append("• Success depends on execution and differentiation")
        confidence = 0.85
        
    else:
        explanations["innovation_reasoning"].append(
            "Your idea shows LOW INNOVATION - it closely resembles existing solutions."
        )
        explanations["innovation_reasoning"].append(
            f"High similarity ({max_similarity:.1%}) suggests an established market category."
        )
        explanations["key_factors"].append("✗ Saturated market with strong incumbents")
        explanations["key_factors"].append("✗ Requires exceptional execution to differentiate")
        confidence = 0.80
    
    # MARKET ANALYSIS
    market_saturation = max_similarity * 100
    if market_saturation < 30:
        explanations["market_analysis"].append(
            "BLUE OCEAN OPPORTUNITY: Low market saturation suggests an underexploited market segment."
        )
    elif market_saturation < 50:
        explanations["market_analysis"].append(
            "MODERATE MARKET: Some competition exists, but room for multiple successful players."
        )
    else:
        explanations["market_analysis"].append(
            "SATURATED MARKET: Many competitors already serve this niche. Differentiation is critical."
        )
    
    # Add top similar ideas analysis
    if top_similar_ideas:
        explanations["market_analysis"].append(
            f"Top competing idea: '{top_similar_ideas[0]['idea']}' (Similarity: {top_similar_ideas[0]['similarity']:.1%})"
        )
        explanations["market_analysis"].append(
            f"This indicates your idea occupies similar market space with some variations."
        )
    
    # METRICS INTERPRETATION
    scalability_score = metrics.get("scalability", 5)
    tech_feasibility = metrics.get("technical_feasibility", 5)
    market_demand = metrics.get("market_demand", 5)
    
    if scalability_score >= 7:
        explanations["key_factors"].append("✓ High scalability potential")
    else:
        explanations["key_factors"].append("• Limited scalability in current market")
    
    if tech_feasibility >= 6:
        explanations["key_factors"].append("✓ Technically achievable with current technology")
    elif tech_feasibility >= 4:
        explanations["key_factors"].append("• Requires moderate R&D and technical expertise")
    else:
        explanations["key_factors"].append("✗ Significant technical challenges require advanced research")
    
    if market_demand >= 7:
        explanations["key_factors"].append("✓ Strong market demand indicators")
    elif market_demand >= 5:
        explanations["key_factors"].append("• Moderate market demand with growth potential")
    else:
        explanations["key_factors"].append("• Uncertain market demand - requires validation")
    
    # RECOMMENDATIONS
    if innovation_score >= 8:
        explanations["recommendations"].append(
            "🎯 PRIORITY: File for patents and protect your IP before competitors enter."
        )
        explanations["recommendations"].append(
            "🎯 STRATEGY: Focus on fast market entry to establish first-mover advantage."
        )
        explanations["recommendations"].append(
            "🎯 NEXT STEP: Conduct extensive customer discovery to validate market fit."
        )
    elif innovation_score >= 6:
        explanations["recommendations"].append(
            "🎯 ACTION: Develop a clear competitive positioning strategy."
        )
        explanations["recommendations"].append(
            "🎯 RESEARCH: Study top 3 competitors to identify unmet customer needs."
        )
        explanations["recommendations"].append(
            "🎯 BUILD: Create an MVP focusing on your unique differentiators."
        )
    else:
        explanations["recommendations"].append(
            "🎯 VALIDATION: Conduct extensive market research to confirm demand."
        )
        explanations["recommendations"].append(
            "🎯 DIFFERENTIATION: Identify and emphasize unique value propositions."
        )
        explanations["recommendations"].append(
            "🎯 EXECUTION: Superior execution and customer experience are critical for success."
        )
    
    # Calculate confidence score based on data quality
    explanations["confidence_score"] = round(confidence, 3)
    
    return explanations


def get_innovation_breakdown(innovation_score: float) -> dict:
    """
    Provide a detailed breakdown of what the innovation score means.
    
    Args:
        innovation_score (float): Innovation score (0-10)
    
    Returns:
        dict: Detailed interpretation
    """
    
    score_range = {
        "0-2": {
            "label": "Commodity Idea",
            "description": "Very similar to many existing solutions. Highly saturated market.",
            "difficulty": "Extremely Hard",
            "advice": "Consider pivoting to a unique angle or different market segment."
        },
        "2-4": {
            "label": "Low Innovation",
            "description": "Established market with multiple competitors offering similar solutions.",
            "difficulty": "Very Hard",
            "advice": "Success requires exceptional execution, brand, or distribution."
        },
        "4-6": {
            "label": "Moderate Innovation",
            "description": "Some new approach or feature, but largely incremental improvements.",
            "difficulty": "Hard",
            "advice": "Build competitive advantages through technology or customer experience."
        },
        "6-8": {
            "label": "High Innovation",
            "description": "Significant differentiation with novel approach to market need.",
            "difficulty": "Medium",
            "advice": "Focus on scaling and capturing market share before competitors respond."
        },
        "8-10": {
            "label": "Breakthrough Innovation",
            "description": "Highly novel idea with potential to create new market category.",
            "difficulty": "Hard (due to market validation uncertainty)",
            "advice": "Prioritize customer validation and first-mover advantage."
        }
    }
    
    # Determine which range the score falls into
    if innovation_score < 2:
        range_key = "0-2"
    elif innovation_score < 4:
        range_key = "2-4"
    elif innovation_score < 6:
        range_key = "4-6"
    elif innovation_score < 8:
        range_key = "6-8"
    else:
        range_key = "8-10"
    
    return {
        "score_range": range_key,
        "breakdown": score_range[range_key]
    }


def generate_success_factors(idea: str, metrics: dict) -> dict:
    """
    Identify key success factors specific to this idea.
    
    Args:
        idea (str): The startup idea
        metrics (dict): Detailed metrics
    
    Returns:
        dict: Success factors analysis
    """
    
    idea_lower = idea.lower()
    success_factors = {
        "critical_factors": [],
        "positive_factors": [],
        "risk_factors": []
    }
    
    # B2B vs B2C analysis
    if any(word in idea_lower for word in ['b2b', 'enterprise', 'saas', 'business']):
        success_factors["critical_factors"].append("Sales & customer acquisition strategy")
        success_factors["critical_factors"].append("Recurring revenue model")
        success_factors["positive_factors"].append("Potential for high LTV:CAC ratio")
    else:
        success_factors["critical_factors"].append("User acquisition and retention")
        success_factors["critical_factors"].append("Network effects or viral growth")
    
    # Tech complexity
    if any(word in idea_lower for word in ['ai', 'ml', 'blockchain', 'quantum', 'biotech']):
        success_factors["critical_factors"].append("Expert technical team with deep domain knowledge")
        success_factors["risk_factors"].append("High R&D costs and longer time to market")
    else:
        success_factors["positive_factors"].append("Lower technical barriers to entry")
    
    # Market accessibility
    if metrics.get("market_demand", 5) >= 7:
        success_factors["positive_factors"].append("Clear market demand validation")
    else:
        success_factors["risk_factors"].append("Uncertain product-market fit requires extensive testing")
    
    # Scalability
    if metrics.get("scalability", 5) >= 7:
        success_factors["positive_factors"].append("Highly scalable business model")
    else:
        success_factors["critical_factors"].append("Unit economics must be optimized for profitability")
    
    # General factors
    success_factors["critical_factors"].extend([
        "Strong founding team with complementary skills",
        "Sufficient capital to reach profitability/series A",
        "Customer-centric product development"
    ])
    
    success_factors["risk_factors"].extend([
        "Competition from larger, well-funded players",
        "Regulatory or compliance changes",
        "Technology disruption in your market"
    ])
    
    return success_factors
