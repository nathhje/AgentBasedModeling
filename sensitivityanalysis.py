# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:35:58 2019

@author: Gebruiker
"""

from helpers.modelv4 import Model
from helpers.make_csv import make_csv
import matplotlib.pyplot as plt
import random

from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

def main():
    
    problem, params = createProblem()
    
    Y = np.zeros([params.shape[0]])
    
    for i, X in enumerate(params):
        Y[i] = evaluate_model(X)
        
    si = sobol.analyze(problem,Y)
    
    print(si['S1'])
    print(si['S2'])

def createProblem():
    problem = {
            'num_vars': 2,
            'names': ['ratio_of_smart_agents', 'number_of_strategies'],
            'bounds': [[0.3, 0.7],
                       [2., 10.]]
            }
    
    param_values = saltelli.sample(problem, 4)
    
    return problem, param_values

def evaluate_model(inputs):
    
    model = Model(inputs[0])
    #print(inputs)
    
    model.make_buyers(int(round(inputs[1])))
    model.make_sellers(int(round(inputs[1])))
    model.run_simulation()
    
    profit = 0
    
    for agent in model.buyers_list:
        profit += agent.profit
        
    for agent in model.sellers_list:
        profit += agent.profit
        
    profit = profit / (len(model.buyers_list) + len(model.sellers_list))
    
    return profit
    

if __name__ == "__main__":
    main()