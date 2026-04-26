"""
SWOT Analysis Generator for Startup Ideas
Generates dynamic Strengths, Weaknesses, Opportunities, and Threats
based on the startup concept and market analysis.
"""

def generate_swot_analysis(idea: str, innovation_score: float, market_match: float, interpretation: str) -> dict:
    """
    Generate a SWOT analysis matrix based on the startup idea and its metrics.
    
    Args:
        idea (str): The startup idea
        innovation_score (float): Innovation score (0-10)
        market_match (float): Market similarity score (0-10)
        interpretation (str): Interpretation of innovation level
    
    Returns:
        dict: SWOT analysis with strengths, weaknesses, opportunities, threats
    """
    
    swot = {
        "strengths": [],
        "weaknesses": [],
        "opportunities": [],
        "threats": []
    }
    
    # STRENGTHS based on innovation and market factors
    if innovation_score >= 7:
        swot["strengths"].append("Highly innovative concept with differentiation potential")
        swot["strengths"].append("Low direct competition in the market")
        swot["strengths"].append("Potential for first-mover advantage")
    else:
        swot["strengths"].append("Proven market demand exists")
    
    if market_match < 0.3:
        swot["strengths"].append("Unique niche positioning opportunity")
    else:
        swot["strengths"].append("Clear target market with existing solutions reference")
    
    # Add idea-specific strengths
    idea_lower = idea.lower()
    if any(word in idea_lower for word in ['ai', 'machine learning', 'automation', 'intelligent']):
        swot["strengths"].append("Leverages cutting-edge AI/ML technology")
    
    if any(word in idea_lower for word in ['sustainable', 'eco', 'green', 'renewable']):
        swot["strengths"].append("Aligns with global sustainability trends")
    
    if any(word in idea_lower for word in ['blockchain', 'web3', 'crypto', 'decentralized']):
        swot["strengths"].append("Positioned in high-growth emerging tech space")
    
    # WEAKNESSES
    if innovation_score < 4:
        swot["weaknesses"].append("High market saturation with existing competitors")
        swot["weaknesses"].append("Requires strong differentiation strategy")
    
    if market_match > 0.7:
        swot["weaknesses"].append("Direct competition from established players")
        swot["weaknesses"].append("Limited blue ocean opportunity")
    
    # General weaknesses
    swot["weaknesses"].append("Early-stage idea needs validation and market research")
    swot["weaknesses"].append("Requires substantial capital for development and launch")
    
    # OPPORTUNITIES
    if innovation_score >= 6:
        swot["opportunities"].append("Potential acquisition target for larger corporations")
        swot["opportunities"].append("Licensing and partnership opportunities")
    
    swot["opportunities"].append("Global market expansion possibilities")
    swot["opportunities"].append("Adjacent product/service extensions")
    
    # Market-specific opportunities
    if 'data' in idea_lower or 'analytics' in idea_lower:
        swot["opportunities"].append("B2B SaaS scalability potential")
    
    if 'social' in idea_lower or 'community' in idea_lower:
        swot["opportunities"].append("Network effects and viral growth potential")
    
    if 'mobile' in idea_lower or 'app' in idea_lower:
        swot["opportunities"].append("Multi-platform expansion (iOS, Android, Web)")
    
    # THREATS
    if market_match > 0.5:
        swot["threats"].append("Established competitors with larger resources")
        swot["threats"].append("Customer switching costs and brand loyalty challenges")
    
    swot["threats"].append("Rapid market evolution and technology changes")
    swot["threats"].append("Economic downturns affecting startup funding")
    swot["threats"].append("Regulatory changes in relevant industry sectors")
    
    # Innovation-specific threats
    if innovation_score >= 8:
        swot["threats"].append("Risk of idea being copied by larger players")
        swot["threats"].append("Uncertain product-market fit validation")
    else:
        swot["threats"].append("Difficulty in defending market position long-term")
    
    return swot


def generate_metrics_breakdown(innovation_score: float, market_match: float) -> dict:
    """
    Generate detailed metrics breakdown for visualization.
    Shows specific dimensions like scalability, technical feasibility, etc.
    
    Args:
        innovation_score (float): Innovation score (0-10)
        market_match (float): Market match score (0-1, converted to 0-10)
    
    Returns:
        dict: Detailed metrics for radar chart visualization
    """
    
    market_match_10 = market_match * 10
    
    # Inverse relationship: high market match = low market saturation
    market_saturation = 10 - market_match_10
    
    # Innovation directly impacts differentiation
    differentiation = innovation_score
    
    # Estimate other metrics
    scalability = min(10, (innovation_score * 0.7) + 3)  # Innovative ideas tend to be more scalable
    technical_feasibility = min(10, 8 - (innovation_score * 0.3))  # More innovative = harder to build
    market_demand = min(10, (11 - market_saturation) * 0.9)  # Inverse of saturation
    
    return {
        "innovation": round(innovation_score, 2),
        "differentiation": round(differentiation, 2),
        "scalability": round(scalability, 2),
        "technical_feasibility": round(technical_feasibility, 2),
        "market_demand": round(market_demand, 2),
        "market_saturation": round(market_saturation, 2)
    }


def generate_pitch_outline(idea: str, innovation_score: float, interpretation: str, swot: dict) -> dict:
    """
    Generate a structured pitch deck outline based on the analysis.
    
    Args:
        idea (str): The startup idea
        innovation_score (float): Innovation score
        interpretation (str): Innovation interpretation
        swot (dict): SWOT analysis
    
    Returns:
        dict: Pitch deck structure with talking points
    """
    
    return {
        "slide_1_hook": {
            "title": "The Opportunity",
            "talking_points": [
                f"Problem: {idea}",
                "Market Gap: Underserved customer needs",
                f"Innovation Level: {interpretation}"
            ]
        },
        "slide_2_solution": {
            "title": "Our Solution",
            "talking_points": [
                f"Core Value Proposition: {idea}",
                f"Key Differentiator: {swot['strengths'][0] if swot['strengths'] else 'Unique approach'}",
                "How it solves the problem uniquely"
            ]
        },
        "slide_3_market": {
            "title": "Market Opportunity",
            "talking_points": [
                "Target Market Size (TAM)",
                "Serviceable Addressable Market (SAM)",
                f"Growth Potential: Based on innovation score of {innovation_score}/10"
            ]
        },
        "slide_4_competition": {
            "title": "Competitive Landscape",
            "talking_points": [
                f"Direct Competitors: {swot['threats'][0] if swot['threats'] else 'Minimal'}",
                f"Competitive Advantages: {', '.join(swot['strengths'][:2])}",
                "Barriers to Entry"
            ]
        },
        "slide_5_business_model": {
            "title": "Business Model",
            "talking_points": [
                "Revenue Streams",
                "Unit Economics",
                "Path to Profitability"
            ]
        },
        "slide_6_traction": {
            "title": "Traction & Milestones",
            "talking_points": [
                "MVP Status",
                "Customer Validation",
                "Upcoming Milestones"
            ]
        },
        "slide_7_team": {
            "title": "Team & Execution",
            "talking_points": [
                "Founder Background",
                "Key Team Members & Expertise",
                "Why we're the right team to execute"
            ]
        },
        "slide_8_financials": {
            "title": "Financial Projections",
            "talking_points": [
                "Revenue Forecast (3-5 years)",
                "Expense Breakdown",
                "Path to Break-even"
            ]
        },
        "slide_9_ask": {
            "title": "The Ask",
            "talking_points": [
                "Funding Amount & Use of Funds",
                "ROI Timeline",
                "Investor Value Proposition"
            ]
        }
    }
