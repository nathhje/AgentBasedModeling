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
    
    def __init__(self, seller):

        """"define if agent is a seller"""
        self.seller = seller

        self.buy_prices = []
        self.sell_prices = []
        self.strategies = Strategies()
        self.match_prices = []
        self.profit = 0
        self.penalty = 0

        self.positivity = random.random()

    """Warming up period, random choosing"""
    def random_choose(self, stock_price_history):
        self.match_prices.append(0)

        if self.seller == True:
            sell_price = stock_price_history[-1] + random.random() - 0.4
            self.sell_prices.append(sell_price)
            return sell_price
        else:
            buy_price = stock_price_history[-1] + random.random() - 0.6
            self.buy_prices.append(buy_price)
            return buy_price

    """Actual agents, choosing based on strategies"""
    def choose(self, stock_price_history):
        weights = self.strategies.choose_strategy()
	
	#add for every turn a new 0
        self.match_prices.append(0)
		
        nextGuess = self.strategies.nextPoint(weights, stock_price_history)
        std_pos = np.std(stock_price_history[-self.strategies.memory-1:]) * self.positivity

        if(self.seller):
            nextGuess += std_pos
            self.sell_prices.append(nextGuess)
        else:
            nextGuess -= std_pos
            self.buy_prices.append(nextGuess)

        return nextGuess 

    """When matched, update the price for which it was matched"""
    #why use match_price[-1] and not match_price.append()?
    def matched(self, price):
        self.match_prices[-1] = price

    """Calculate profit based on current stock and current marketprice"""	
    def calcProfit(self, marketprice):
        if self.match_prices[-1] == 0:
            self.profit += self.penalty
            return
		
        # Can this be removed?
        if len(self.match_prices) < 1:
            return
		
        if self.seller:
            self.profit += self.match_prices[-1] - marketprice
        else:
            self.profit += marketprice - self.match_prices[-1]

    def track_strategies(self, stock_price_history):
        for i in self.strategies.strategies:
            print(i)
            print(stock_price_history)
            