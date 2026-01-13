import numpy as np
import pandas as pd

np.random.seed(2026)

tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "META", "AMZN", "TSLA", "JPM", "JNJ", "XOM"]

cost_basis_ranges = {
    "AAPL": (100, 180),
    "MSFT": (180, 350),
    "NVDA": (150, 500),
    "GOOGL": (1000, 1600),
    "META": (150, 350),
    "AMZN": (2000, 3500),
    "TSLA": (400, 900),
    "JPM": (120, 200),
    "JNJ": (130, 190),
    "XOM": (60, 120),
}

sectors = {
    "AAPL": "Technology",
    "MSFT": "Technology",
    "NVDA": "Technology",
    "GOOGL": "Communication Services",
    "META": "Communication Services",
    "AMZN": "Consumer Discretionary",
    "TSLA": "Consumer Discretionary",
    "JPM": "Financials",
    "JNJ": "Healthcare",
    "XOM": "Energy",
}

portfolio = pd.DataFrame({
    "Ticker": tickers,
    "Shares": np.random.randint(5, 30, size=len(tickers)),
    "Cost_Basis": [np.random.randint(*cost_basis_ranges[t]) for t in tickers],
    "Sector": [sectors[t] for t in tickers],
})

portfolio.to_csv("portfolio_holdings.csv", index=False)
print("Saved: portfolio_holdings.csv")
