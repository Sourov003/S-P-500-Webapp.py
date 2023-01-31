import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
import pandas as pd
import numpy as np

from prophet.plot import plot_plotly
from plotly import graph_objs as go


START = "2015-01-01" 
TODAY = date.today().strftime("%Y-%m-%d")

st.title = ("Stock Prediction App")

stocks = ("APPL","GOOGL","MSFT", "GME", "DE")
selected_stocks = st.selectbox("Select Dataset for Prediction", stocks)

n_year = st.slider("Year's of Prediction", 1, 4)
period = n_year * 365






#Simple stock data
import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
#   Simple Stock App
 
Shown are the stock **closing price** and **volume** of Google!



""")
 
# Ask user for a ticker symbol
ticker_symbol = st.text_input("Enter a ticker symbol (e.g. AAPL)")
tickerData = yf.Ticker(ticker_symbol)
st.write(tickerData)
 
# Open a stock dataframe using yfinance library.GOOGL)

tickerData = yf.Ticker(ticker_symbol)

#Get the Historical data of the Stock
("""
## Volume

""") 
tickerDf = tickerData.history(period = '1m',start='2004-07-14', end='2023-01-01')
# tickerDf = tickerData.history(period='1M', start='2022-12-01', end='2023-01-27')



st.write("""
## Closing price


""") 
# Show closing price of the stock.GOOGL)

st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.High) 
# st.line_chart(tickerDf.Low) 
# st.line_chart(tickerDf.Open) 
# st.line_chart(tickerDf.Dividend),
# st.line_chart(tickerDf.Split)
# st.line_chart(tickerDf.StockSplits)   
# st.line_chart(tickerDf.StockDividends) 
# st.line_chart(tickerDf.StockSplits)
