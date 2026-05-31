import os
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

claude = LLM(
    model="anthropic/claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)


def create_agents():
    market_researcher = Agent(
        role="Market Research Analyst",
        goal="Research market size, trends, and recent news for the given company or product",
        backstory=(
            "You're a seasoned market analyst who digs deep into industry data, trends, "
            "and news to surface insights that matter for product strategy. You always back "
            "claims with specific numbers and cite sources."
        ),
        tools=[search_tool],
        llm=claude,
        verbose=True,
        allow_delegation=False,
    )

    competitor_analyst = Agent(
        role="Competitive Intelligence Analyst",
        goal="Map the competitive landscape, identifying key players, their strengths, weaknesses, and positioning",
        backstory=(
            "You specialize in competitive intelligence with a talent for identifying what makes "
            "companies win or lose in their markets. You go beyond surface-level comparisons and "
            "find the strategic moves that matter."
        ),
        tools=[search_tool],
        llm=claude,
        verbose=True,
        allow_delegation=False,
    )

    strategy_writer = Agent(
        role="Product Strategy Writer",
        goal="Synthesize research into a clear, actionable competitive intelligence report",
        backstory=(
            "You're a former McKinsey consultant turned product strategist. You turn raw research "
            "into crisp, executive-ready reports with specific, opinionated recommendations. "
            "You never write vague advice — every recommendation is concrete and justified."
        ),
        llm=claude,
        verbose=True,
        allow_delegation=False,
    )

    return {
        "market_researcher": market_researcher,
        "competitor_analyst": competitor_analyst,
        "strategy_writer": strategy_writer,
    }
