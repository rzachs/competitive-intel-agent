import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

load_dotenv()


def validate_env():
    missing = [k for k in ("ANTHROPIC_API_KEY", "SERPER_API_KEY") if not os.getenv(k)]
    if missing:
        print(f"Error: missing environment variables: {', '.join(missing)}")
        print("Copy .env.example to .env and fill in your keys.")
        sys.exit(1)


def run(company: str, product: str = "") -> str:
    subject = f"{company} {product}".strip()
    print(f"\nStarting competitive intelligence analysis for: {subject}\n")

    agents = create_agents()
    tasks = create_tasks(agents, company, product)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    report = str(result)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"report_{company.replace(' ', '_').lower()}_{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Competitive Intelligence Report: {subject}\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        f.write(report)

    print(f"\nReport saved to: {filename}")
    return report


if __name__ == "__main__":
    validate_env()

    company = input("Company or product to analyze: ").strip()
    if not company:
        print("Error: company name is required.")
        sys.exit(1)

    product = input("Specific product (optional, press Enter to skip): ").strip()

    run(company, product)
