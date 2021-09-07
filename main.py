import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
#Simple Stock Price App
Shown are the stock closing 

""")

tickerSymbol ='GOOGl'
tickerData=yf.Ticker(tickerSymbol)
tickerDf =tickerData.history(period='1d', start='2010-5-31', end ='2021-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)