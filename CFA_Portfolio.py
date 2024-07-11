#Case Study :
#Build up $10,000 investment portfolios containing four stocks.
#Use Case 1: Will have an equal weighting between the stocks.
#Use Case 2: Will be optimized with weighing allocation that provides the best retun.

#Importing Required Packages :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Evaluate the required stock price and assign it to variable to stock_list:
stock_list = ['AMD','AAPL','MSFT','ORCL']

print(np.arange(1,13,2))
#Create an empty dictionary to store the stock info
stocks = {}
for i_stock in stock_list:
    stock[i_stock] = pd.read_csv(str(i_stock + '.csv'),
                                 parse_dates=True,index_col='Date')