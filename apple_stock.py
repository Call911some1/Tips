import streamlit as st
import pandas as pd
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
import yfinance as yf

warnings.filterwarnings('ignore')

st.write('# Приложение для анализа цены акций компании Apple')

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2024-9-3')

st.write("### 1. Цена зыкрытия **AAPL**")
st.line_chart(tickerDf.Close)

st.write("### 2. Объём акций AAPL")
st.line_chart(tickerDf.Volume)