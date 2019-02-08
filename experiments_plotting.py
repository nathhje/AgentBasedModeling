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
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in reader: #for each iteration
            params1.append(row)

    memory = []
    profit = []
    matches = []
    type_agent = []

    for row in params1:
        results = []
        for my_string in row:
            result = []
            for x in my_string.split():
                try:
                    y = float(x.strip(",").strip("[").strip("]"))
                    result.append(y)
                except:
                    result.append(x.strip(",").strip("[").strip("]").strip("'"))
            results.append(result)

        memory.append(results[0])
        profit.append(results[1])
        matches.append(results[2])
        type_agent.append(results[3])

    # print(memory_list)
    # print(len(memory_list))
    # e.g. read other datasets

    """ Plot the experiments """
    plot_experiment1(memory, profit, type_agent)
    # plot_experiment2(eval_memory, profit)
    plot_experiment3(memory, matches, type_agent)

""" Plot experiments """
def plot_experiment1(memory, profit, type_agent):
    """ Memory vs Profit (agent level) """
    #DRAFT FOR 1 ITERATION
    memory = memory[0]
    profit = profit[0]
    type_agent = type_agent[0]
    # print(type_agent)


    plt.figure()
    m_b = []
    m_s = []
    p_b = []
    p_s = []
    # for iteration in enumerate(type_agent): #FOR ALL ITERATIONS
    for idx, agent in enumerate(type_agent): #iteration
        # print(idx, agent)
        # print(type_agent[idx])
        # print(memory[idx])
        if agent == 'Buyer':
            m_b.append(memory[idx])
            p_b.append(profit[idx])
            # plt.plot(memory[idx], profit[idx], c= 'b', label='Buyer')
        else:
            m_s.append(memory[idx])
            p_s.append(profit[idx])
            # plt.plot(memory[idx], profit[idx], c= 'r', label='Seller')

    plt.scatter(m_b, p_b, c= 'b', label='Buyer')
    plt.scatter(m_s, p_s, c= 'r', label='Seller')
    plt.title('The profit of agents with different memory')
    plt.xlabel('Memory')
    plt.ylabel('Profit')
    plt.legend(loc='best')
    plt.show()
    plt.tight_layout()
    plt.savefig('exp_data/experiment1.png')

def plot_experiment2(eval_memory, profit):
    """ Strategy evaluation memory vs Profit (agent level) """
    # unnecessary?
    plt.show()

def plot_experiment3(memory, match_number, type_agent):
    """ Memory vs Match number (agent level) """
    #DRAFT FOR 1 ITERATION
    memory = memory[0]
    match_number = match_number[0]
    type_agent = type_agent[0]

    plt.figure()
    mem_b = []
    mem_s = []
    match_b = []
    match_s = []
    # for iteration in enumerate(type_agent): #FOR ALL ITERATIONS
    for idx, agent in enumerate(type_agent): #iteration
        # print(idx, agent)
        # print(type_agent[idx])
        # print(memory[idx])
        if agent == 'Buyer':
            mem_b.append(memory[idx])
            match_b.append(match_number[idx])
            # plt.plot(memory[idx], profit[idx], c= 'b', label='Buyer')
        else:
            mem_s.append(memory[idx])
            match_s.append(match_number[idx])
            # plt.plot(memory[idx], profit[idx], c= 'r', label='Seller')

    plt.scatter(mem_b, match_b, c= 'b', label='Buyer')
    plt.scatter(mem_s, match_s, c= 'r', label='Seller')
    plt.title('The number of matches of agents with different memory')
    plt.xlabel('Memory')
    plt.ylabel('Number of matches')
    plt.legend(loc='best')
    plt.show()
    plt.tight_layout()
    plt.savefig('exp_data/experiment3.png')


if __name__ == '__main__':
    main()
