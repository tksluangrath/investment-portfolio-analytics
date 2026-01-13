# 📊 Investment Portfolio Analytics Platform

## Overview
The **Investment Portfolio Analytics Platform** is an end-to-end analytics project that evaluates portfolio performance, attribution, and risk using historical market data. The project combines a Python data pipeline with an interactive Tableau dashboard to deliver clear, finance-focused insights.

The project is structured in **phases**, allowing incremental expansion from valuation and performance reporting into deeper risk analytics.

---

## Objectives
- Analyze portfolio market value and performance over time  
- Identify key contributors to unrealized gains and losses  
- Provide clear, executive-style KPIs as of the latest available market date  
- Lay the foundation for portfolio risk and volatility analysis  

---

## Data Sources
- **Yahoo Finance** (via `yfinance`)
  - Historical adjusted closing prices for selected equities
- **Simulated Portfolio Holdings**
  - Randomized share counts and cost basis for demonstration purposes

---


---

## Key Datasets

### `portfolio_holdings.csv`
Simulated portfolio holdings used as the base portfolio.

| Column | Description |
|------|------------|
| Ticker | Stock ticker symbol |
| Shares | Number of shares held |
| Cost_Basis | Purchase price per share |
| Sector | Industry sector |

---

### `prices_long.csv`
Daily adjusted closing prices in long format.

| Column | Description |
|------|------------|
| Date | Trading date |
| Ticker | Stock ticker |
| Adj_Close | Adjusted closing price |

---

### `portfolio_prices.csv`
Merged dataset used directly in Tableau for valuation and performance analysis.

| Column | Description |
|------|------------|
| Market_Value | Shares × Adjusted Price |
| Cost_Value | Shares × Cost Basis |
| Unrealized_PnL | Market Value − Cost Value |
| Unrealized_PnL_Pct | Unrealized P&L / Cost Value |
| Cumulative_Return | Return relative to first observation |
| As_Of_Date | Data generation date |

---

### `returns_long.csv` (Phase 2)
Daily returns generated for future risk and volatility analysis.

| Column | Description |
|------|------------|
| Daily_Return | Day-over-day percentage return |

---

## Tableau Dashboard (Phase 1)

### Key Views
- **Total Portfolio Value (KPI)**
- **Total Unrealized P&L (KPI)**
- **Portfolio ROI % (KPI)**
- **Portfolio Market Value Over Time**
- **Largest Unrealized Gains & Losses by Security**
- **Portfolio Allocation by Sector**

### Design Principles
- Snapshot KPIs filtered to the **latest trading date**
- Time-series charts unfiltered to preserve historical trends
- Conditional coloring for gains vs losses
- Clear labeling of assumptions and date context

---

## Phase 2: Risk & Volatility Analysis (Planned)
Phase 2 extends the platform into portfolio risk analytics using daily returns.

Planned additions:
- Volatility by security (annualized)
- Rolling volatility over time
- Drawdown analysis
- Risk vs return scatterplots
- Portfolio-level risk KPIs

---

## Tools & Technologies
- **Python**: pandas, numpy, yfinance
- **Tableau**: Dashboard design and interactive analytics
- **GitHub**: Version control and documentation

---

## Assumptions & Notes
- Portfolio holdings are simulated for demonstration purposes
- Historical performance applies **current holdings** to past prices
- No transaction costs, dividends, or rebalancing are modeled

---

## Future Enhancements
- Sharpe ratio and risk-adjusted metrics
- Sector-level risk contribution
- Correlation heatmaps
- Scenario stress testing

---

## Author
**Terrance Luangrath**  
MS in Data Science (in progress)  
Focus: Analytics, Financial Data Science, and Visualization


