import yfinance as yf
import pandas as pd
from datetime import date

# Capture current date once
today = date.today().isoformat()

# Tickers and date range
TICKERS = [
    "AAPL", 
    "MSFT", 
    "NVDA", 
    "GOOGL", 
    "META", 
    "AMZN", 
    "TSLA", 
    "JPM", 
    "JNJ", 
    "XOM"]

START_DATE = "2010-01-01"
END_DATE = today

# Download adjusted prices
prices = yf.download(
    TICKERS,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=True,
    progress=False
)

# Convert wide -> long 
close_wide = prices["Close"].reset_index()

prices_long = close_wide.melt(
    id_vars="Date",
    var_name="Ticker",
    value_name="Adj_Close"
).dropna()

# Save for CSV
prices_long.to_csv("prices_long.csv", index=False)
print("Saved: prices_long.csv")

# Daily returns (for risk charts)
returns_long = prices_long.sort_values(["Ticker", "Date"]).copy()
returns_long["Daily_Return"] = returns_long.groupby("Ticker")["Adj_Close"].pct_change()

returns_long.to_csv("returns_long.csv", index=False)
print("Saved: returns_long.csv")
