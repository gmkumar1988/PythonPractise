# # int_a = 8
# # print(int_a)
# # type(-8)
# # boolean_a = True
# # type(boolean_a)
# string_a = "Hello"
# type(string_a)
# print("Hello")
# print(string_a)
# print("I can't fly")
# print('Net'+'Profit')
# print(float(556))
# print(str(2>1))
#
# number = 5
# print(str(number) + "Euros")
# list_a =["Mahesh","Senthil","Manas","Mirula"]
# # list_b = (12,304,392,239)
# # print(list_b)
# # print(list_a[3])
# # list_b.sort()
# # # print(list_b.sort())
# # a = (12,30,23)
# # print(a)
# # print(a.sort())
# dict_a = {'first_name':'Frank',
#           'second_name':'Furt'}
# print(dict_a['first_name'])
#
# x = 3
# print(x>3 and x<4)
#
# import math as mth
# print(mth.sqrt(81))
# from math import sqrt
# print(sqrt(100))
# from math import *
#
# a=3
# b =2
# if a>b:
#     print("A is greater than B")
# #
#
# # customer_list = (50,30,40)
# # for i_customer in customer_list :
# #     if (i_customer > 15):
# #     else: print("Low")
#
# import numpy as np
# np.array([0,1,2])
# import pandas as pd
# makers = ['a','b','c']
# list1 = [12,34,5]
# array_1 = np.array([15,30,45])
# dict_1 = {'d':20,'e':30,'f':50}
# print(dict_1)
# print(pd.Series(data = list1))
# print(pd.Series(data= list1, index=makers))
#
# import numpy as np
#
# frames = np.array([[1,2,3,4],[3,4,5,6]])
# print(frames)
#
# array_3 = np.arange(40)
# print(array_3)
# print(np.random.rand(10))
# print(np.random.randint(10,30))
# print(np.random.randint(10,20,4))
import pandas as pd
# import pandas_datareader as pdr
# print(pdr.DataReader('005930','naver','2022-01-01','2022-01-31'))

# import yfinance as yf
# stock = 'GOOG'
# start_date = '2024-01-04'
# end_date = '2024-07-01'
# stocks_yf = yf.download(stock,start =start_date,end = end_date)
# # print(stocks_yf)
# dataframe_3 = pd.read_csv("/Users/maheshg/Downloads/Python Fundamentals - Learner Files/C2 - Loading & Cleaning Data/2 - Complete/Data Source.csv")
# # print(dataframe_3.info)
# # pd.to_datetime(dataframe_3['Date'])
# dataframe_3['Date'] = pd.to_datetime(dataframe_3['Date'])
# print(dataframe_3.info)
# print(dataframe_3.isna())
# print(dataframe_3.isna().sum())
# print(dataframe_3.dropna())
# print(dataframe_3.dropna(axis=1))

import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
# stocks_yf = yf.download(stock,start =start_date,end = end_date)

#creating stocksand bonds dataframe
stocks = pd.read_csv('/Users/maheshg/Downloads/Python Fundamentals - Learner Files/C4 - Visualizing Data/2 - Complete/stocks.csv',
                     parse_dates=True,index_col='Date')[['Adj Close']]

bonds = pd.read_csv('/Users/maheshg/Downloads/Python Fundamentals - Learner Files/C4 - Visualizing Data/2 - Complete/bonds.csv',
                     parse_dates=True,index_col='Date')[['Adj Close']]

oils = pd.read_csv('/Users/maheshg/Downloads/Python Fundamentals - Learner Files/C4 - Visualizing Data/2 - Complete/oil.csv',
                     parse_dates=True,index_col='Date')[['Adj Close']]

print(stocks.head())
print(bonds.head())
print(oils.head())
stocks_bonds_oil = pd.concat(['stocks','bonds'])
print(stocks_bonds_oil)