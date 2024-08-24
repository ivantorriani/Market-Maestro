import pandas as pd
import numpy as np  # Use np.nan instead of importing nan directly
import pandas_ta as ta
import yfinance as yf


def monitor_stock(ticker):
    data = yf.download(ticker, period="1mo", interval="1d")  # Get last month's data
    data['Resistance'] = data['High'].rolling(window=20).max()
    data['Breakout'] = data['Close'] > data['Resistance']
    
    # Check the latest entry to see if there's a breakout
    if data['Breakout'].iloc[-1]:
        print(f"Breakout detected for {ticker} on {data.index[-1].date()}")
        # Consider placing a buy order here based on your strategy
    else:
        print(f"No breakout for {ticker} as of {data.index[-1].date()}")

# Example usage:
monitor_stock("BTAI")