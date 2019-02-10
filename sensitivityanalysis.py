# -*- coding: utf-8 -*-
"""
This file contains the Sobol sensitivity analysis for the model. When running 
this file, three functions can be called at the bottom that all have different 
purposes. create_samples creates a list of input samples for the analysis,
evaluate creates an output for each input sample and analysis analyses these
outputs. Before calling the first two functions, one has to make certain that
the right input and output files are available. These functions should therefore
each be run only once. (create_samples adds to samples.py and evaluate takes
data from samples.py and adds to outcomes.py)
"""

from helpers.modelv4 import Model
import matplotlib.pyplot as plt
import random
import csv

from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np


""" Computes the output data for the sensitivity analysis by running the model
for a list of input data """
def evaluate():
    
    """input data"""
    params = []
    
    """the input data is retrieved"""
    fileread = 'sadata/samples.csv'
    with open(fileread, 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        
        for row in reader:
            
            params.append(row)
    
    """runs the model and saves the outcomes for each input sample"""
    for i, X in enumerate(params):
        Y = run_model(X)
        filename = 'sadata/outcomes.csv'
        
        with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            row = X+Y
            writer.writerow(row)
            
            """print to keep track of where the program is"""
            print(X+Y)
                
""" Creates a list of input data for the sensitivity analysis and saves this data """
def create_samples():
    
    """samples are created"""
    problem, params = create_problem()
    
    """samples are saved"""
    filename = 'sadata/samples.csv'
    with open(filename, 'a', newline = '') as csvfile:
    
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
        for row in params:
            
            writer.writerow(row)
         
    """samples are printed"""
    for i, X in enumerate(params):
        print(i,X)
        
""" Performs sensitivity analysis on the output data and plots it """
def analysis(output):
    
    """the input samples are determined for the analysis"""
    problem, params = create_problem()
    
    """the output data is retrieved"""
    Y = np.zeros([params.shape[0]])
    i = 0
    
    fileread = 'sadata/outcomes.csv'
    with open(fileread, 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        
        for row in reader:
            
            Y[i] = row[output]
            i += 1
    
    """the analysis is performed"""
    si = sobol.analyze(problem,Y,print_to_console=True)
    
    """the result of the analysis is plotted"""
    plots(si,output)
    
""" Makes a plot of the result of the sensitivity analysis """
def plots(data, output):
    
    """it is determined what type of output is being plotted"""
    variable = "average number of matches a smart agent made"
    color = 'r'
    
    if output==5:
        variable = "average profit a smart agent made"
        color = 'b'
        
    elif output == 7:
        variable = "stability of the market"
        color = 'g'
    
    """the lists for the plot are created"""
    x = ['random','strategies','memory','evaluation','agents','random total','strategies total','memory total','evaluation total','agents total','random and strategies', 'random and memory', 'random and evaluation', 'random and agents', 'strategies and memory', 'strategies and evaluation', 'strategies and agents', 'memory and evaluation', 'memory and agents','evaluation and agents']
    y = list(data['S1']) + list(data['ST'])
    error = list(data['S1_conf']) + list(data['ST_conf'])
    for i in range(4):
        y += list(data['S2'][i][i+1:])
        error += list(data['S2_conf'][i][i+1:])
    
    """the plot is made"""
    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    plt.bar(x,y, yerr=error, color = color)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    
    plt.xlabel('factor(s)')
    plt.ylabel('influence')
    plt.title('The influence of the input factors \n on the %s'%variable)
    plt.show()

""" Creates a problem and input samples for the Sobol analysis """
def create_problem():
    
    """the problem"""
    problem = {
            'num_vars': 5,
            'names': ['ratio_of_random_agents', 'number_of_strategies', 'memory','evaluation', 'agent_number'],
            'bounds': [[0., 1.],
                       [2., 10.],
                       [2., 50.],
                       [1.,10.],
                       [20.,80.]]
            }
    
    """the input samples that go with the problem"""
    param_values = saltelli.sample(problem, 1000)
    
    return problem, param_values

""" Runs and evaluates the model for a set of input variables """
def run_model(inputs):
    
    random.seed(4)
    
    """the model is initialised and the number of buyers and sellers set"""
    model = Model(inputs[0])
    model.number_of_buyers = int(round(inputs[4]))
    model.number_of_sellers = int(round(inputs[4]))
    
    """buyers and sellers are created with the right number of strategies"""
    model.make_buyers(int(round(inputs[1])))
    model.make_sellers(int(round(inputs[1])))
    
    """for each buyer and seller the memory and strategy evaluation memory are
    set """
    for buyer in model.buyers_list:
        buyer.strategies.create_strategies(int(round(inputs[2])))
        buyer.strategy_evaluation_memory = int(round(inputs[3]))
    for seller in model.sellers_list:
        seller.strategies.create_strategies(int(round(inputs[2])))
        seller.strategy_evaluation_memory = int(round(inputs[3]))
        
    """model is run"""
    model.run_simulation()
    
    """the agent level output"""
    profit = 0
    matches = 0
    smarts = 0
    
    """average profit and average number of matches per smart agent are determined """
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
    
    """the stock level output"""
    stock = 0
    
    """the variance in the stock market is determined"""
    for i in range(model.warming_up_time, model.end_time):
        stock += model.stock_price_history[i]
    
    price_number = model.end_time-model.warming_up_time
    
    stock = stock / price_number
    
    variance = 0
    
    for i in range(model.warming_up_time, model.end_time):
        
        variance += (model.stock_price_history[i] - stock) ** 2
    
    variance = variance / price_number
    
    """the three outputs are returned"""
    return [profit, matches, variance]
    

""" Run create_samples() to create a file with input samples
Run evaluate() to evaluate the model for each input sample and create output
Run analysis(output_variable) to analyse the output and make plots.
output_variable can 5 for the average profit of a smart agent, 6 for the
average number of matches of a smart agent and 7 for the variance in the stock
market """
if __name__ == "__main__":
    output_variable = 6
    analysis(output_variable)