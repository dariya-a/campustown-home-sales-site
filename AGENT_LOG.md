# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-10: Median sale price bar chart

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then add a horizontal bar chart of the median sale price for each city above the table on index.html. Keep the table and the $10,000 rule as they are"
- **Agent produced:** `scripts/city_median_sale_price.py`, which writes `data/city_median_sale_price.json` from the CSV (median of sales of $10,000 or more, per city). `index.html` now draws the horizontal bar chart from that file. The page had no table or $10,000 rule to keep, so none was added.
- **Checked or changed:** The agent checked the medians against the SQLite file for the top and bottom cities, and confirmed that 40 rows fall under $10,000, matching the description sheet. It rendered the page at desktop and phone widths with no horizontal overflow. Still to check: the live page after the change is merged to main.
