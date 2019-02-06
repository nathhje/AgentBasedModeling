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
    
    def __init__(self, seller, unique_id, strategy_number, isitrandom):

        """"define if agent is a seller, 
            if the agent uses random strategies and apply its ID number"""
        self.seller = seller
        self.id = unique_id
        self.random = isitrandom

        """create empty lists for keeping track of buy/sell prices"""
        self.buy_prices = []
        self.sell_prices = []

        """create strategies"""
        self.strategies = Strategies(strategy_number)
        self.strategy_evaluation = []
        for i in range(self.strategies.number_of_strategies):
            self.strategy_evaluation.append([])
        self.strategy_index = []

        """empty list for keeping track of the prices for which the agent matched
           count the amount of matches and the profit it made"""
        self.match_prices = []
        self.match_count = 0
        self.profit = 0

        """constants"""
        self.positivity = random.random()
        self.set_period = 3

    """random choosing strategy"""
    def random_choose(self, stock_price_history):
        
        self.match_prices.append(0)
        self.strategy_index.append(0)

        """calculate sell/buy price the agent will offer"""
        if self.seller == True:
            sell_price = stock_price_history[-1] + 5 * (random.random() - 0.4)
            self.sell_prices.append(sell_price)
            return sell_price
        else:
            buy_price = stock_price_history[-1] + 5 * (random.random() - 0.6)
            self.buy_prices.append(buy_price)
            return buy_price

    """fixed choosing strategy"""
    def fixed_choose(self, stock_price_history):

        self.match_prices.append(0)
        self.strategy_index.append(0)

        """devide the price history to check in parts"""
        period = round(max(300,len(stock_price_history))/self.set_period)

        """calculate sell/buy price agent will offer"""
        if (np.mean(stock_price_history[-period:-1]) > np.mean(stock_price_history[-2*period:-period]) and self.seller):
            return self.random_choose(stock_price_history)
        elif(np.mean(stock_price_history[-period:-1]) < np.mean(stock_price_history[-2*period:-period]) and not self.seller):
            return self.random_choose(stock_price_history)
        elif(self.seller):
            sell_price = stock_price_history[-1] + 5
            self.sell_prices.append(sell_price)
            return sell_price
        else:
            buy_price = stock_price_history[-1] - 5
            self.buy_prices.append(buy_price)
            return buy_price

    """pick the one of the strategies that would have performed the best within strategy_evaluation_memory"""
    def choose_strategy(self):
        
        strategy_evaluation_sums = [sum(i) for i in self.strategy_evaluation]
        index = strategy_evaluation_sums.index(min(strategy_evaluation_sums))
        self.strategy_index.append(index)
        return self.strategies.strategies[index]

    """choosing based on strategies"""
    def choose(self, stock_price_history, weights):

        """normalization if stock market history is shorter than the memory"""
        length_diff = len(weights) - len(stock_price_history) + 1
        if length_diff > 0:
            weights = weights[length_diff:]
            self.strategies.normalize_weights(weights)

        """calculate sell/buy price agent will offer"""
        next_guess = self.strategies.next_point(weights, stock_price_history)
        std_pos = np.std(stock_price_history[-self.strategies.memory-1:]) * self.positivity

        if(self.seller):
            next_guess += std_pos
        else:
            next_guess -= std_pos

        return next_guess 

    """When matched, update the price for which it was matched"""
    def matched(self, price):

        self.match_prices[-1] = price
        self.match_count += 1

    """Calculate profit based on current stock and current marketprice"""	
    def calcProfit(self, marketprice):

        """avoid exceptions"""
        if len(self.match_prices) < 1:
            return

        """when no match was made, the profit stays zero"""
        if self.match_prices[-1] == 0:
            return

        """when match was made, calculate the profit"""
        if self.seller:
            self.profit += self.match_prices[-1] - marketprice
        else:
            self.profit += marketprice - self.match_prices[-1]

    """create a list to keep track of how well the strategies worked in the past"""
    def initial_track_strategies(self, stock_price_history):

        for i in reversed(range(1, min(self.strategies.strategy_evaluation_memory, len(stock_price_history)))):
            for j in range(len(self.strategies.strategies)):
                history_mod = stock_price_history[:-i]
                weights_mod = self.strategies.strategies[j][-len(stock_price_history)+1:-i]
                self.strategies.normalize_weights(weights_mod)
                self.strategy_evaluation[j].append(abs(self.choose(history_mod, weights_mod) - stock_price_history[-i]))

    """checks whether the max_length is already reached. 
       If so, the first element is removed before a new last element is added"""
    def track_strategies(self, stock_price_history, best_aim):

        for i in range(len(self.strategy_evaluation)):
            if self.strategies.strategy_evaluation_memory == len(self.strategy_evaluation[i]):
                self.strategy_evaluation[i].pop(0)
            self.strategy_evaluation[i].append(abs(self.choose(stock_price_history[:-1],self.strategies.strategies[i]) - best_aim))
        return self.strategy_evaluation

