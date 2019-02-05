# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:35:58 2019

@author: Gebruiker
"""

from helpers.modelv4 import Model
from helpers.make_csv import make_csv
import matplotlib.pyplot as plt
import random
import csv

from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np


def main():
    '''
    
    
    #Y = np.zeros([params.shape[0]])
    #print(Y)
    '''
    
    params = []
    
    fileread = 'sadata/samples_jasper3_3.csv'
    with open(fileread, 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        
        for row in reader:
            
            params.append(row)
        
        
    
    
    for i, X in enumerate(params):
        #print(i,X)
        Y = evaluate_model(X)
        filename = 'sadata/outcomes_jasper3_3.csv'
        
        with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            row = X+Y
            writer.writerow(row)
            print(X+Y)
                
        
    #si = sobol.analyze(problem,Y,print_to_console=True)
    
    #print(si['S1'])
    #print(si['S2'])
    
def createSamples():
    problem, params = createProblem()
    print(params)
    
    filename = 'sadata/samples.csv'
    with open(filename, 'a', newline = '') as csvfile:
    
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in params:
            
            writer.writerow(row)
    for i, X in enumerate(params):
        print(i,X)
    

def createProblem():
    problem = {
            'num_vars': 5,
            'names': ['ratio_of_random_agents', 'number_of_strategies', 'memory','evaluation', 'agent_number'],
            'bounds': [[0., 1.],
                       [2., 10.],
                       [2., 50.],
                       [1.,10.],
                       [20.,80.]]
            }
    
    param_values = saltelli.sample(problem, 1000)
    
    return problem, param_values

def evaluate_model(inputs):
    random.seed(4)
    
    model = Model(inputs[0])
    #print(inputs)
    model.number_of_buyers = int(round(inputs[4]))
    model.number_of_sellers = int(round(inputs[4]))
    
    model.make_buyers(int(round(inputs[1])))
    model.make_sellers(int(round(inputs[1])))
    
    for buyer in model.buyers_list:
        buyer.strategies.create_strategies(int(round(inputs[2])))
        buyer.strategy_evaluation_memory = int(round(inputs[3]))
    for seller in model.sellers_list:
        seller.strategies.create_strategies(int(round(inputs[2])))
        seller.strategy_evaluation_memory = int(round(inputs[3]))
    model.run_simulation()
    
    profit = 0
    matches = 0
    smarts = 0
    
    for agent in model.buyers_list:
        if not agent.random:
            profit += agent.profit
            matches += agent.match_count
            smarts += 1
    
    for agent in model.sellers_list:
        if not agent.random:
            profit += agent.profit
            matches += agent.match_count
            smarts += 1
        
    if smarts > 0:
        profit = profit / smarts
        matches = matches / smarts
    
    stock = 0
    
    for i in range(model.warming_up_time, model.end_time):
        stock += model.stock_price_history[i]
    
    price_number = model.end_time-model.warming_up_time
    
    stock = stock / price_number
    
    variance = 0
    
    for i in range(model.warming_up_time, model.end_time):
        
        variance += (model.stock_price_history[i] - stock) ** 2
    
    variance = variance / price_number
    print(profit)
    print(matches)
    return [profit, matches, variance]
    

if __name__ == "__main__":
    main()