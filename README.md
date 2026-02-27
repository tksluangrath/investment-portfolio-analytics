# Investment Portfolio Analytics Platform

A project that analyzes portfolio performance, risk, and attribution using historical market data. Built with Python for the data pipeline and Tableau for visualization. I'm building this in phases, starting with basic performance metrics and eventually expanding into deeper risk analytics.

## What This Does

The platform lets you:
- Track portfolio market value and performance over time
- See which positions are driving gains or losses
- View executive-level KPIs as of the most recent trading date
- Lay groundwork for portfolio risk and volatility analysis (coming in Phase 2)

## Data Sources

**Market data:** Yahoo Finance (pulled via `yfinance`) for historical adjusted closing prices

**Portfolio holdings:** Simulated data with randomized share counts and cost basis - this is for demonstration purposes since I don't have access to real portfolio data

## The Datasets

### portfolio_holdings.csv
The base portfolio with simulated positions.

| Column | What it is |
|--------|-----------|
| Ticker | Stock symbol |
| Shares | Number of shares owned |
| Cost_Basis | What you paid per share |
| Sector | Industry sector |

### prices_long.csv
Daily adjusted closing prices in long format - basically every ticker's price history stacked vertically.

| Column | What it is |
|--------|-----------|
| Date | Trading date |
| Ticker | Stock ticker |
| Adj_Close | Adjusted closing price |

### portfolio_prices.csv
This is the merged dataset that Tableau uses for all the valuation and performance analysis.

| Column | What it is |
|--------|-----------|
| Market_Value | Current value (shares × price) |
| Cost_Value | What you paid (shares × cost basis) |
| Unrealized_PnL | Profit/loss (market value - cost) |
| Unrealized_PnL_Pct | P&L as a percentage |
| Cumulative_Return | Return from the first date |
| As_Of_Date | When the data was generated |

### returns_long.csv (Phase 2)
Daily returns calculated for future risk and volatility work.

| Column | What it is |
|--------|-----------|
| Daily_Return | Day-over-day percentage return |

## The Tableau Dashboard (Phase 1)

Right now the dashboard shows:
- Total portfolio value (KPI)
- Total unrealized P&L (KPI)
- Portfolio ROI % (KPI)
- Portfolio market value over time (line chart)
- Biggest winners and losers by position (bar chart)
- Portfolio breakdown by sector (pie/tree map)

**Design choices I made:**
- KPIs show the latest trading date only (what's the portfolio worth right now?)
- Time-series charts show full history (so you can see trends)
- Color-coded gains (green) vs losses (red)
- Clear labels showing assumptions and date context

## What's Coming in Phase 2: Risk & Volatility

Once Phase 1 is solid, I'll add:
- Volatility by security (annualized standard deviation)
- Rolling volatility over time
- Drawdown analysis (how much the portfolio has fallen from peaks)
- Risk vs return scatterplots
- Portfolio-level risk metrics like Sharpe ratio

## Tools Used

- **Python:** pandas, numpy, yfinance for data processing
- **Tableau:** Dashboard design and interactive visualizations
- **GitHub:** Version control

## Important Assumptions

A few things to keep in mind:
- Portfolio holdings are simulated - this is a demonstration project
- I'm applying current holdings retroactively to historical prices (not modeling how the portfolio actually evolved)
- No transaction costs, dividends, or rebalancing included
- This is for learning and showcasing analytics skills, not real investment advice

## What I'd Add Later

Beyond Phase 2, some ideas:
- Sharpe ratio and other risk-adjusted return metrics
- Sector-level risk contribution analysis
- Correlation heatmaps between positions
- Scenario stress testing (what happens if the market drops 20%?)

## Contact

**Author**: Terrance Luangrath

**📧 Email:** [tksluangrath@gmail.com](mailto:tksluangrath@gmail.com)  
**💼 LinkedIn:** [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/terranceluangrath/)  
**👨‍💻 GitHub:** [![GitHub](https://img.shields.io/badge/GitHub-181717.svg?logo=github&logoColor=white)](https://github.com/tksluangrath)

---

*MS in Data Science (in progress) | Focus: Analytics, Financial Data Science, and Visualization*
