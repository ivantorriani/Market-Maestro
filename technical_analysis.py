import pandas as pd
import numpy as np  # Use np.nan instead of importing nan directly
import pandas_ta as ta
import yfinance as yf


def breakout_status(ticker):
    data = yf.download(ticker, period="1mo", interval="1d")  # Get last month's data
    data['Resistance'] = data['High'].rolling(window=20).max()
    data['Breakout'] = data['Close'] > data['Resistance']
    
    # Check the latest entry to see if there's a breakout
    if data['Breakout'].iloc[-1]:
        print(f"Breakout detected for {ticker} on {data.index[-1].date()}")
        # Consider placing a buy order here based on your strategy
    else:
        print(f"No breakout for {ticker} as of {data.index[-1].date()}")

def check_high_volume(ticker):
    # Download historical data
    data = yf.download(ticker, period="1mo", interval="1d")
    
    # Calculate volume average
    data['Volume_Avg'] = data['Volume'].rolling(window=20).mean()
    
    # Detect high volume
    data['High_Volume'] = data['Volume'] > data['Volume_Avg']
    
    # Check the latest entry
    if data['High_Volume'].iloc[-1]:
        print(f"High volume detected for {ticker} on {data.index[-1].date()}")
    else:
        print(f"No high volume for {ticker} as of {data.index[-1].date()}")

def detect_cup_and_handle(ticker):
    # Download historical data
    data = yf.download(ticker, period="6mo", interval="1d")
    
    # Use TA indicators (SMA for smooth curve)
    data['SMA20'] = ta.sma(data['Close'], length=20)
    
    # Detect rounded bottom by checking if SMA20 is U-shaped
    data['U_Shaped'] = (data['SMA20'].diff(10) < 0) & (data['SMA20'].diff(-10) > 0)
    
    # Detect handle by looking for a short consolidation after U-shape
    data['Handle'] = data['Close'].rolling(window=5).mean() < data['Close'].rolling(window=20).mean()
    
    # Confirm breakout if price rises above the handle
    data['Breakout'] = data['Close'] > data['Close'].rolling(window=10).max()
    
    # Identify Cup and Handle Pattern
    data['Cup_and_Handle'] = data['U_Shaped'] & data['Handle'] & data['Breakout']
    
    if data['Cup_and_Handle'].iloc[-1]:
        print(f"Cup and Handle detected for {ticker} on {data.index[-1].date()}")
    else:
        print(f"No Cup and Handle detected for {ticker} as of {data.index[-1].date()}")
    
    return data

def detect_double_bottom(ticker):
    # Download historical data
    data = yf.download(ticker, period="6mo", interval="1d")
    
    # Detect double bottom by checking if two lows are at the same level
    data['Low_1'] = data['Low'].rolling(window=5).min()
    data['Low_2'] = data['Low'].shift(5).rolling(window=5).min()
    data['Double_Bottom'] = (abs(data['Low_1'] - data['Low_2']) < data['Low'].mean() * 0.02)
    
    # Confirm breakout above intermediate high
    data['Breakout'] = data['Close'] > data['Close'].rolling(window=5).max().shift(10)
    
    data['Double_Bottom_Pattern'] = data['Double_Bottom'] & data['Breakout']
    
    if data['Double_Bottom_Pattern'].iloc[-1]:
        print(f"Double Bottom detected for {ticker} on {data.index[-1].date()}")
    else:
        print(f"No Double Bottom detected for {ticker} as of {data.index[-1].date()}")
    
    return data

def detect_ascending_triangle(ticker):
    # Download historical data
    data = yf.download(ticker, period="6mo", interval="1d")
    
    # Horizontal resistance detection
    data['Resistance'] = data['Close'].rolling(window=20).max()
    
    # Ascending support detection
    data['Support'] = data['Close'].rolling(window=20).min()
    data['Ascending_Support'] = data['Support'].diff() > 0
    
    # Confirm breakout above resistance
    data['Breakout'] = data['Close'] > data['Resistance']
    
    data['Ascending_Triangle'] = data['Ascending_Support'] & data['Breakout']
    
    if data['Ascending_Triangle'].iloc[-1]:
        print(f"Ascending Triangle detected for {ticker} on {data.index[-1].date()}")
    else:
        print(f"No Ascending Triangle detected for {ticker} as of {data.index[-1].date()}")
    
    return data

'''
def check_rsi_momentum(ticker, start="2024-08-01", end="2024-08-23", rsi_period=14):
    # Load historical data
    data = yf.download(ticker, start=start, end=end)
    
    # Calculate RSI
    data['RSI'] = data.ta.rsi(length=rsi_period)
    
    # Check if RSI is moving from oversold to the 50-70 range
    data['RSI_oversold'] = data['RSI'] < 30
    data['RSI_above_30'] = data['RSI'] > 30
    data['RSI_moving_up'] = data['RSI'].diff() > 0

    # Print the conditions columns for inspection
    print("RSI Conditions:\n", data[['RSI', 'RSI_oversold', 'RSI_above_30', 'RSI_moving_up']].head(20))
    
    # Find rows where RSI is moving from oversold to above 30
    potential_buy = data[data['RSI_oversold'] & data['RSI_above_30'] & data['RSI_moving_up']]

    return potential_buy[['Close', 'RSI']]

def detect_macd_crossover(ticker, start="2023-01-01", end="2023-08-23"):
    # Load historical data
    data = yf.download(ticker, start=start, end=end)
    
    # Calculate MACD
    macd = ta.macd(data['Close'])
    
    if macd is not None:
        data = data.join(macd)
        
        # Correct column names
        macd_line = 'MACD'
        signal_line = 'MACDs'
        
        # Detect MACD crossover
        data['MACD_Crossover'] = data[macd_line] > data[signal_line]  # MACD Line above Signal Line
        data['MACD_Crossover_Previous'] = data[macd_line].shift(1) <= data[signal_line].shift(1)  # Previous Crossover Check
        
        # Find rows where a crossover has occurred
        crossovers = data[data['MACD_Crossover'] & data['MACD_Crossover_Previous']]
        
        return crossovers[['Close', macd_line, signal_line]]
    else:
        print("MACD calculation returned None.")
        return pd.DataFrame()  # Return an empty DataFrame if MACD is None

# Example usage
macd_crossovers = detect_macd_crossover("AAPL")
print(macd_crossovers)

'''