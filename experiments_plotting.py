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

def main():
    """ Read all the datafiles """
    params1 = []

    fileread1 = 'exp_data/dataset1.csv'
    with open(fileread1, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        for row in reader: #for each iteration
            params1.append(row)

    # print(params[0])
    l = list(params1[0])
    print(type(l))
    print(l)
    memory = l[0]
    profit = l[1]
    matches = l[2]
    type_agent = l[3]

    # print(memory, profit)
    print(len(memory), len(profit), len(matches), len(type_agent))
    # print(len(l[0]), len(l[1]), len(l[2]))
    print(l[0])
    print(memory)
    for i in memory:
        print(i)
    # for i in params): #for each iteration
    #     print(i)
    #     memory.append(i)
    #     profit.append(i)
    #     type_agent.append(i)

    """ Plot the experiments """
    plot_experiment1(memory, profit)

""" Plot experiments """
def plot_experiment1(memory, profit):
    """ Memory vs Profit (agent level) """
    plt.figure()
    plt.scatter(memory, profit) #, c= type_agent)
    plt.title('The profit of agents with different memory')
    plt.xlabel('Time')
    plt.ylabel('Profit')
    plt.show()
    plt.tight_layout()
    plt.savefig('exp_data/experiment1.png')

def plot_experiment2(eval_memory, profit):
    """ Strategy evaluation memory vs Profit (agent level) """
    plt.show()

def plot_experiment3(memory, match_number):
    """ Memory vs Match number (agent level) """
    plt.show()


if __name__ == '__main__':
    main()
