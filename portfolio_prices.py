import pandas as pd
from datetime import date

# Load data
portfolio = pd.read_csv("portfolio_holdings.csv")
prices_long = pd.read_csv("prices_long.csv", parse_dates=["Date"])

# Clean join keys
portfolio["Ticker"] = (
    portfolio["Ticker"]
    .astype(str)
    .str.upper()
    .str.strip()
)

prices_long["Ticker"] = (
    prices_long["Ticker"]
    .astype(str)
    .str.upper()
    .str.strip()
)

# Detect price column name
price_col = "Adj_Close" if "Adj_Close" in prices_long.columns else "Price"
if price_col not in prices_long.columns:
    raise ValueError(f"Expected a price column named 'Adj_Close' or 'Price'. Found: {prices_long.columns.tolist()}")

# Coerce numeric
portfolio["Shares"] = pd.to_numeric(
    portfolio["Shares"], 
    errors="coerce")

portfolio["Cost_Basis"] = pd.to_numeric(
    portfolio["Cost_Basis"], 
    errors="coerce")

prices_long[price_col] = pd.to_numeric(
    prices_long[price_col], 
    errors="coerce")

# Drop missing essentials (DO NOT fill prices with 0)
portfolio = portfolio.dropna(subset=["Ticker", "Shares", "Cost_Basis"])
prices_long = prices_long.dropna(subset=["Date", "Ticker", price_col])

# Join
portfolio_prices = prices_long.merge(
    portfolio, 
    on="Ticker", 
    how="inner")

# Metrics
portfolio_prices["Market_Value"] = portfolio_prices["Shares"] * portfolio_prices[price_col]
portfolio_prices["Cost_Value"] = portfolio_prices["Shares"] * portfolio_prices["Cost_Basis"]
portfolio_prices["Unrealized_PnL"] = portfolio_prices["Market_Value"] - portfolio_prices["Cost_Value"]
portfolio_prices["Unrealized_PnL_Pct"] = portfolio_prices["Unrealized_PnL"] / portfolio_prices["Cost_Value"]

portfolio_prices = portfolio_prices.sort_values(["Ticker", "Date"])
portfolio_prices["Cumulative_Return"] = (
    portfolio_prices.groupby("Ticker")[price_col]
    .transform(lambda s: s / s.iloc[0] - 1)
)

try:
    portfolio_prices.to_csv("portfolio_prices.csv", index=False)
except PermissionError:
    import os
    # Try to close any file handles and retry
    csv_file = "portfolio_prices.csv"
    if os.path.exists(csv_file):
        try:
            os.remove(csv_file)
        except:
            pass
    portfolio_prices.to_csv("portfolio_prices.csv", index=False)

print("Saved: portfolio_prices.csv")
print("Date range:", portfolio_prices["Date"].min(), "→", portfolio_prices["Date"].max())
