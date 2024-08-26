# imports and such - - - - - - - - - - - - - - - - - - -
import yfinance as yf
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.timeseries import TimeSeries
from halo import Halo

api_key = 'weingas'

fd = FundamentalData(key=api_key, output_format='pandas')

# Examples
# stock = yf.Ticker('AAPL')
#financials = stock.financials
#balance_sheet = stock.balance_sheet
#cash_flow = stock.cashflow
#recommendations = stock.recommendations
#news = stock.news
#dividends = stock.dividends
#earnings = stock.earnings

#Could potentially analyze the news with another text scanner

# fundamental analysis  - - - - - - - - - - - - - - - - - - - - - -



def get_general_info(ticker):

    stock = yf.Ticker(ticker)

    gen_info = stock.history(start='2024-06-01', end='2024-08-25')

    return gen_info

def get_timely_info(ticker):
    
    stock = yf.Ticker(ticker)

    timely_info = stock.info

    return timely_info

def get_financials(ticker):

    stock = yf.Ticker(ticker)
    
    financials = stock.financials

    return financials

def get_balance_sheet(ticker):

    stock = yf.Ticker(ticker)

    balance_sheet = stock.balance_sheet

    return balance_sheet

def get_cash_flow(ticker):

    stock = yf.Ticker(ticker)

    cash_flow = stock.cash_flow

    return cash_flow

def get_earnings(ticker):

    stock = yf.Ticker(ticker)

    earnings = stock.earnings

    return earnings





