# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:45:28 2019

@author: my favorite team
"""

import random
import math
import numpy as np
from classes.strategiesv3 import Strategies

class Agent():
    
    def __init__(self, seller, unique_id, strategy_number):

        """"define if agent is a seller"""
        self.seller = seller
        self.id = unique_id
		
        self.buy_prices = []
        self.sell_prices = []
        self.strategies = Strategies(strategy_number)
        self.strategy_evaluation = []
        for i in range(self.strategies.number_of_strategies):
            self.strategy_evaluation.append([])
        self.match_prices = []
        self.match_count = 0
        self.profit = 0

        self.positivity = random.random()
		
        self.strategy_index = []
        self.random = False

    """Warming up period, random choosing"""
    def random_choose(self, stock_price_history):
        self.random = True
        self.match_prices.append(0)
        self.strategy_index.append(0)
        if self.seller == True:
            sell_price = stock_price_history[-1] + 5 * (random.random() - 0.4)
            self.sell_prices.append(sell_price)
            return sell_price
        else:
            buy_price = stock_price_history[-1] + 5 * (random.random() - 0.6)
            self.buy_prices.append(buy_price)
            return buy_price

		#if len(stock_price_history) == 1:
        #    smart_guess = stock_price_history[-1]
        #else:
        #    smart_guess = 2 * stock_price_history[-1] - stock_price_history[-2]
        #
        #if self.seller == True:
        #    sell_price = smart_guess + 2 * (random.random() - 0.4)
        #    self.sell_prices.append(sell_price)
        #    return sell_price
        #else:
        #    buy_price = smart_guess + 2 * (random.random() - 0.6)
        #    self.buy_prices.append(buy_price)
        #    return buy_price

    """pick the one of the strategies that would have performed the best within strategy_evaluation_memory"""
    def choose_strategy(self):
        
        strategy_evaluation_sums = [sum(i) for i in self.strategy_evaluation]
        index = strategy_evaluation_sums.index(min(strategy_evaluation_sums))
        self.strategy_index.append(index)
        #random strategy
        #index = math.floor(random.random()*len(self.strategies.strategies))
        #calculated best strategy
        #index = determine_best_strategies(marketprice, strategy_memory)
        return self.strategies.strategies[index]

    """Actual agents, choosing based on strategies"""
    def choose(self, stock_price_history, weights):
        length_diff = len(weights) - len(stock_price_history) +1 
        if length_diff > 0:
            #print(length_diff)
            #print(weights[length_diff:])
            weights = weights[length_diff:]
            self.strategies.normalize_weights(weights)
		
        nextGuess = self.strategies.nextPoint(weights, stock_price_history)
        std_pos = np.std(stock_price_history[-self.strategies.memory-1:]) * self.positivity

        if(self.seller):
            nextGuess += std_pos
        else:
            nextGuess -= std_pos

        return nextGuess 

    """When matched, update the price for which it was matched"""
    #why use match_price[-1] and not match_price.append()?
    def matched(self, price):
        self.match_prices[-1] = price
        self.match_count += 1

    """Calculate profit based on current stock and current marketprice"""	
    def calcProfit(self, marketprice):
        if self.match_prices[-1] == 0:
            return
		
        # Can this be removed?
        if len(self.match_prices) < 1:
            return
		
        if self.seller:
            self.profit += self.match_prices[-1] - marketprice
        else:
            self.profit += marketprice - self.match_prices[-1]



    def initial_track_strategies(self, stock_price_history):
        for i in reversed(range(1, min(self.strategies.strategy_evaluation_memory, len(stock_price_history)))):
            for j in range(len(self.strategies.strategies)):
                #print(self.strategy_evaluation_memory)
                #if i == 0:
                #    history_mod = stock_price_history[:]
                #    weights_mod = self.strategies.strategies[j][-len(stock_price_history)+1:]

                    #print(i, stock_price_history[:], stock_price_history, weights, weights[-len(stock_price_history)+1:])
                    #print(self.choose(stock_price_history[:], weights[-len(stock_price_history)+1:]))
                #else:
                history_mod = stock_price_history[:-i]
                weights_mod = self.strategies.strategies[j][-len(stock_price_history)+1:-i]
                    #print(i, stock_price_history[:-i], stock_price_history, weights, weights[-len(stock_price_history)+1:-i])
                #normalizes weights_mod
                self.strategies.normalize_weights(weights_mod)
                #print(history_mod, weights_mod)
                #print(i, j, self.choose(history_mod, weights_mod), stock_price_history[-i])
                self.strategy_evaluation[j].append(abs(self.choose(history_mod, weights_mod) - stock_price_history[-i]))
        #print(self.strategy_evaluation)

    def track_strategies(self, stock_price_history):
        #checks whether the max_lenght is already reached. If so, the first element is removed before a new last element is added
        for i in range(len(self.strategy_evaluation)):
            if self.strategies.strategy_evaluation_memory == len(self.strategy_evaluation[i]):
                self.strategy_evaluation[i].pop(0)
            #print(stock_price_history[:-1])
            self.strategy_evaluation[i].append(abs(self.choose(stock_price_history[:-1],self.strategies.strategies[i]) - stock_price_history[-1]))
        return self.strategy_evaluation

