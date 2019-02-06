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

"""Experiment 1: Memory vs profit (agent level)"""
def run_experiment1(iterations):
    for X in range(iterations):
        Y = experiment1(X)
        filename = 'results/experiment1.csv'

        with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            row = Y
            writer.writerow(row)
            print(row)

def experiment1(iterations):
    random.seed(1)

    model = Model(0.5)
    model.make_buyers(3)
    model.make_sellers(3)
    model.run_simulation()

    memory = []
    profit = []
    type_agent = []
    for agent in model.buyers_list:
        if not agent.random:
            memory.append(agent.strategies.memory)
            profit.append(agent.profit)
            type_agent.append('Blue')

    for agent in model.sellers_list:
        if not agent.random:
            memory.append(agent.strategies.memory)
            profit.append(agent.profit)
            type_agent.append('Red')
    # plt.figure()
    # plt.scatter(memory, profit, c= type_agent)
    # plt.show()
    return [memory, profit, type_agent]


"""START PROGRAM"""
def main():
    iterations = 7
    # run experiments
    run_experiment1(iterations)
    # experiment1(iterations)
    # experiment2(iterations)
    # experiment3(iterations)
    # experiment4(iterations)
    # experiment8(iterations)


if __name__ == '__main__':
    main()
