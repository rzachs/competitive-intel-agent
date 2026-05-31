# Competitive Intelligence Agent

A multi-agent system that researches a company or product and produces a structured competitive intelligence report. Built with CrewAI + Claude.

## How it works

Three agents run sequentially:
1. **Market Researcher** — searches for market size, trends, and news
2. **Competitor Analyst** — maps the competitive landscape
3. **Strategy Writer** — synthesizes everything into an executive report

The output is a Markdown report saved to your project folder.

## Setup

### 1. Get your API keys

- **Anthropic (Claude)**: https://console.anthropic.com/settings/keys
- **Serper** (web search, free tier = 2500 searches/month): https://serper.dev

### 2. Create your `.env` file

```bash
cp .env.example .env
```

Then open `.env` and fill in your keys.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or with uv (faster):

```bash
pip install uv
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
```

### 4. Run it

```bash
python main.py
```

You'll be prompted to enter a company name (e.g. `Notion`, `Figma`, `Linear`) and optionally a specific product.

The report is saved as `report_<company>_<timestamp>.md` in the same folder.

## Example

```
Company or product to analyze: Notion
Specific product (optional, press Enter to skip): AI

→ Saves: report_notion_20250531_1430.md
```

## Model

Uses `claude-sonnet-4-6` by default. To switch models, change the `model` value in `agents.py`:
- Faster / cheaper: `anthropic/claude-haiku-4-5-20251001`
- Most capable: `anthropic/claude-opus-4-8`
