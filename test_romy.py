# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:42:36 2019

@author: Gebruiker
"""

from helpers.modelv4 import Model
from helpers.make_csv import make_csv
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import seaborn as sns

#CHECK EXPERIMENTS ON GITHUB:
# Memory vs Profit (agent level)
# Strategy evaluation memory vs Profit (agent level)
# Memory vs Match number (agent level)
# Strategy evaluation memory vs Match number (agent level)
# Feed in real market data --> So how our market deviates
# Seed different markets to check how agents perform in them


#Experiment 1: How does memory influence the market?
#Experiment x: In which kind of market does a
#particular strategy perform better?
#Experiment x: How does memory and strategy influence
#the profit of the agent?
#Experiment x: How well does the agent react on
# a real stock market?
#Experiment x: which strategy works the best for the buyers?
#Experiment x: Which strategy works the best for the sellers?

def run_real_market():
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

    # #Plot with pandas - fast
    # print(data)
    # df = df.sort_values('Date') #Just to be sure
    #
    # plt.figure()
    # plt.plot(df['Date'], df['Price'], color='blue', label='Real stock market')
    # plt.title('Stock market')
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.legend(loc='best')
    # plt.show()
    # plt.savefig('results/real_stockmarket.png')

    #Plot with lists - long runtime
    dates = df['Date'].tolist()
    prices = df['Price'].tolist()
    return dates, prices


def experiment1(modelA):
    #Experiment 1 - memory and profit over time
    memory = [x for x in range(1,6)]
    memory = [1, 5, 10, 30]
    plt.figure()

    for i in memory:
        profit_buyer, profit_seller = [], []
        for agent in modelA.buyers_list:
            agent.strategies.memory= i
            profit_buyer.append(agent.profit)
        for agent in modelA.sellers_list:
            agent.strategies.memory = i
            profit_seller.append(agent.profit)
        # index_nr = memory.index(i)
        plt.plot(range(len(profit_buyer)), profit_buyer, label='Buyer m =' + str(i))
        plt.plot(range(len(profit_seller)), profit_seller, label='Seller m =' + str(i))
    plt.title('The profits of agents with different memory')
    plt.xlabel('Time')
    plt.ylabel('Profit')
    plt.legend(loc='best')
    plt.savefig('results/experiment1.png')
    plt.show()

def experiment2(modelA):
    #Experiment 2 - memory vs profit
    memory_buyer, profit_buyer = [], []
    memory_seller, profit_seller = [], []
    memory = [x for x in range(1,60,10)]
    plt.figure()

    for i in memory:
        for agent in modelA.buyers_list:
            agent.strategies.memory = i
            memory_buyer.append(agent.strategies.memory)
            profit_buyer.append(agent.profit)
        for agent in modelA.sellers_list:
            agent.strategies.memory = i
            memory_seller.append(agent.strategies.memory)
            profit_seller.append(agent.profit)
        plt.scatter(memory_buyer, profit_buyer, c='red', label='Buyer m =' + str(i))
        plt.scatter(memory_seller, profit_seller, c='blue',label='Seller m =' + str(i))
    plt.title('Memory and profit')
    plt.xlabel('Memory')
    plt.ylabel('Profit')
    plt.legend(loc='best')
    plt.savefig('results/experiment2.png')
    plt.show()

def experiment3(modelA):
    #Experiment 3 - boxplot
    #Example: http://seaborn.pydata.org/examples/grouped_boxplot.html
    has_memory, has_profit, agent_list = [], [], []

    memory = [x for x in range(1,6)]

    for i in memory:
        for agent in modelA.buyers_list:
            agent.strategies.memory = i
            has_memory.append(agent.strategies.memory)
            has_profit.append(agent.profit)
            agent_list.append('Buyer')
        for agent in modelA.sellers_list:
            agent.strategies.memory = i
            has_memory.append(agent.strategies.memory)
            has_profit.append(agent.profit)
            agent_list.append('Seller')

    sns.set(style="ticks", palette="pastel")

    # x = memory
    # y = profit
    # hue = buyer/seller
    df = pd.DataFrame(np.column_stack([agent_list, has_memory, has_profit]), columns=['agent_list','has_memory','has_profit'])
    print(df)
    sns.boxplot(x="has_memory", y="has_profit",
                hue="agent_list", palette=["m", "g"], data=df)
    sns.despine(offset=10, trim=True)
    plt.show()
    #WHAAAAAAAHHH IT DOESNT WORK


def experiment4(modelA):
    #Experiment 2 - Strategy evaluation memory vs Profit (agent level)
    #experiment 1 with strategy_evaluation_memory


def experiment5(modelA):
    #Experiment 4: Agent and real stock market
    plt.figure()

    dates, prices = run_real_market()
    plt.plot(dates, prices, color='blue', label='Real stock market')
    plt.title('Stock market2')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.savefig('results/experiment4.png')
    plt.show()



### START PROGRAM ###
def main():

    random.seed = 1
    modelA = Model(0.5)
    modelA.make_buyers(3)
    modelA.make_sellers(3)
    modelA.run_simulation()

    # run experiments
    # experiment1(modelA)
    # experiment2(modelA)
    # experiment3(modelA)
    # experiment4(modelA)
    # experiment5(modelA)


if __name__ == "__main__":
    main()
