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
from datetime import datetime
import csv

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

"""Dataset1: Memory, profit, matches, type_agent (agent level) """
def make_dataset1(iterations):
    for X in range(iterations):
        Y = dataset1(X)
        filename = 'exp_data/dataset1.csv'

        with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            row = Y
            writer.writerow(row)
            print(row)

def dataset1(iterations):
    # random.seed(1)

    model = Model(0.5)
    model.make_buyers(3)
    model.make_sellers(3)
    model.run_simulation()

    memory = []
    profit = []
    matches = []
    type_agent = []
    for agent in model.buyers_list:
        if not agent.random:
            memory.append(agent.strategies.memory)
            profit.append(agent.profit)
            matches.append(agent.match_count)
            type_agent.append('Buyer') #Blue

    for agent in model.sellers_list:
        if not agent.random:
            memory.append(agent.strategies.memory)
            profit.append(agent.profit)
            matches.append(agent.match_count)
            type_agent.append('Seller') #Red
    return [memory, profit, matches, type_agent]


"""START PROGRAM"""
def main():
    iterations = 7
    # make datasets
    make_dataset1(iterations)



if __name__ == '__main__':
    main()
