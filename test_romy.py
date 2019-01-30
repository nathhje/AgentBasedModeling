# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:42:36 2019

@author: Gebruiker
"""

from helpers.modelv4 import Model
from classes.strategiesv3 import Strategies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Experiment 1: How does memory influence the market?
#Experiment 2: In which kind of market does a
#particular strategy perform better?
#Experiment 3: How does memory and strategy influence
#the profit of the agent?
#Experiment 4: How well does the agent react on
# a real stock market?
#Experiment x: which strategy works the best for the buyers?
#Experiment x: Which strategy works the best for the sellers?

#Import the data csv file
#Dataset obtained from: https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs/home
data = []
df = pd.read_csv('a.us.txt')

#combine attributes
#combine high and low by avg
#combine open and close by avg
#combine avgHighLow and avgOpenClose
df['Price'] = (df['High'] + df['Low'] + df['Open'] + df['Close'])/4

#Drop obsolete columns for faster processing
drop_columns = ['High', 'Low', 'Open', 'Close', 'Volume','OpenInt']
df = df.drop(labels=drop_columns, axis=1)

#Date to datetime and append df to data
df['Date'] = pd.to_datetime(df['Date'])
data.append(df)

#Plot
print(data)

df = df.sort_values('Date')
x =df['Date']
y= df['Price']

plt.figure()
plt.plot(x, y, color='blue', label='Real stock market')
plt.title('Stock market')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.show()
