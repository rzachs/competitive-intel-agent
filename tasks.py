from crewai import Task


def create_tasks(agents: dict, company: str, product: str = "") -> list:
    subject = f"{company} {product}".strip()

    market_research = Task(
        description=f"""Research the market for {subject}. Cover:
- Market size (current and projected) with specific figures
- Key industry trends over the last 12 months
- Recent news and developments about {company}
- Primary target customer segments
- Any tailwinds or headwinds affecting the space

Be specific. Use numbers. Cite sources where possible.""",
        expected_output=(
            "A structured market research summary with: market size figures, "
            "3-5 key trends, recent company news, and target segments. Bullet point format."
        ),
        agent=agents["market_researcher"],
    )

    competitor_analysis = Task(
        description=f"""Analyze the competitive landscape for {subject}. Cover:
- Top 5 direct competitors with a brief profile of each
- Each competitor's key strengths and weaknesses
- Pricing and positioning strategies
- Recent competitor moves (funding, product launches, partnerships)
- Where {company} stands relative to the field

Go beyond obvious names — include emerging challengers if relevant.""",
        expected_output=(
            "A competitor breakdown covering top 5 players, their strengths/weaknesses, "
            "positioning, and recent moves. Include a summary of where the subject stands."
        ),
        agent=agents["competitor_analyst"],
        context=[market_research],
    )

    strategy_report = Task(
        description=f"""Using the market research and competitor analysis, write a full competitive intelligence report for {subject}.

Structure:
1. Executive Summary (3-4 sentences, the TL;DR a CEO would read)
2. Market Opportunity (size, growth, why now)
3. Competitive Landscape (key dynamics, who's winning and why)
4. SWOT Analysis (4 bullets per quadrant, be specific)
5. Strategic Recommendations (top 3, each with a rationale)
6. Risks to Watch (top 3)

Be opinionated. Avoid vague advice. Write for a product or executive audience.""",
        expected_output=(
            "A complete competitive intelligence report in clean Markdown, "
            "ready to share with a leadership or product team."
        ),
        agent=agents["strategy_writer"],
        context=[market_research, competitor_analysis],
    )

    return [market_research, competitor_analysis, strategy_report]
