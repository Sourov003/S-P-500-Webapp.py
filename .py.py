import streamlit as st
from datetime import date
from datetime import datetime
import yfinance as yf
from yfd import YahooFinanceTimeSeriesByQueryScraper
from prophet import Prophet
import pandas as pd
import numpy as np
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import requests
import urllib3
import urllib3.request




st.title = ("Stock Prediction App")


st.write("""
# Simple Stock App
 Shown are the stock **closing price**, ** Volume**, ** High ** and ** Low**!
Made with Streamlit and Prophet Liberies!         
Made possible sources code on guided project and some own implementation from Sourov :D
""")

st.sidebar.title("Stock Prediction App")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
start_date = st.sidebar.date_input("Start")
end_date = st.sidebar.date_input("End")

data = yf.download(ticker, start = start_date, end = end_date)
#st.write("this is the Opening price chart of " + ticker)
st.subheader("Open Price Chart")
st.line_chart(data.Open)

st.subheader("Close Price Chart")
st.line_chart(data.Close)

st.subheader("Volume Chart")
st.line_chart(data.Volume)

st.subheader("High Price Chart")
st.line_chart(data.High)

st.subheader("Low Price Chart")
st.line_chart(data.Low)



pricing_data, fundamental_data, news, openai1  = st.tabs(["Pricing Data", "Fundamental Data", "News", "OpenAI CHATGPT"])

with pricing_data:
    st.header('price movements')
    data2 = data
    data2['%change'] = data2['Adj Close'] / data2['Adj Close'].shift(1) - 1
    data2.dropna(inplace=True)
    st.write(data2)
    #annualized_returns = data2['%change'].pct_change(10%)
    annual_return = data2['%change'].mean()*252*100
    st.write('Annual Return is ', annual_return, '%')
st.write(data)



with fundamental_data:
    st.header('fundamental data')
    st.write(data)


with news:
    st.header('news')



with pricing_data:
    CAGR = data2['%change'].mean()*(1/252) *1
    st.write('CAGR is ', CAGR, '%')
    volatility = data2['%change'].std()*(1/252) *1
    st.write('Volatility is ', volatility, '%')


from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    key = 'ZGAVFTSK5NK21CM9'
    fd = FundamentalData(key,output_format='pandas')
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_quarterly(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_quarterly(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cash Flow')
    cash_flow = fd.get_cash_flow_quarterly(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)
