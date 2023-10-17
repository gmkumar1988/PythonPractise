import pandas as pd
import yfinance as yf
import numpy as np

#Getting Ticket from Yahoo Finance Package
stock_data = yf.Ticker("^GSPC")

#Getting historical data - 5 years
df_history = stock_data.history(period = "5y")

#Head of df_history
df_history.head()
# print(df_history.columns())

# print(df_history.head())
df_history['Close'].std()
df_history['Close'].min()
df_history['Close'].max()
x = df_history[df_history['Close'] > 3000]
print(x)

y = list(df_history.columns)
print(y)