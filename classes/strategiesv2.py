# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:48:08 2019

@author: my favorite team
"""

import random
import math

class Strategies():

    def __init__(self):
        self.threshold_low_price = 8
        self.threshold_high_price = 12
        self.n_time = 7
        self.memory = 3
        self.weights_dict = {0:0, 1:3, 2:1, 3:1}
        self.optimistic_pessimistic = 0.1
        
    def optimistic(self, history_self, history_all):
        """Agent tries to sell for 1 more than the market value last turn."""
        self.price = history_all[-1] + 1
        return self.price

    def pesimistic(self, history_self, history_all):
        """Agent tries to sell for 1 less than the market value last turn."""
        self.price = history_all[-1] - 1
        return self.price

    def predict_last_2(self, history_self, history_all):
        """Agent predicts the new selling price based on the pregression 
        of the last two steps. """
        if len(history_all) >= 2:
            self.price = history_all[-1] + (history_all[-1]-history_all[-2])
        else:
            self.price = history_all[-1]
        return self.price

    def predict_weighted_last_n(self, history_self, history_all):
        """Agent predicts the new selling/buying price based on the progression 
        of the last n, n-1, n-2..., 2 steps. n is determined by the variable 
        self.memory and the length of history_all. The selling/buying price 
        determined is a weighted average of the predicitons for the different lines.
        The weights are determined are stored in weights_dict. 
        """
        print(self.memory, self.weights_dict)
        print(self.optimistic_pessimistic)
        if self.memory >= len(history_all):
            max_length_of_line = len(history_all)
        else:
            max_length_of_line = self.memory
        sum_price = 0
        sum_weights = 0
        for i in range(max_length_of_line):
            sum_price += self.weights_dict[i] * (history_all[-1] + (history_all[-1]-history_all[-(i+1)]))
            sum_weights += self.weights_dict[i]
        #in case none of the values available so far have any weights assigned to them
        #the agents just resort to taking the last value of the stock.
        #Otherwise a divide by zero error occurs.
        if sum_weights == 0:
            self.price = history_all[-1] + self.optimistic_pessimistic
        else:
            self.price = sum_price/sum_weights + self.optimistic_pessimistic
        return self.price

"""Sellers strategies"""
""" #Agent sell if current price is above the threshold
    def sell_strat_above(self, history_self, history_all):
        if history_all[-1] > self.threshold_high_price:
            self.choice = -1
        else:
            self.choice = self.do_nothing_strat(history_self,history_all)
        return self.choice

    #Agent sell if after n times dropping the price, the price rices
    def sell_strat_after(self,history_self,history_all):
        self.choice = -1
        highest_price = history_all[-self.n_time]
        for price in history_all[-self.n_time+1:-1]:
            if(highest_price < price):
                highest_price = price
            else:
                self.choice = 0
        return self.choice

    def sell_strat_hist_time(self,history_self,history_all):
        return self.choice
"""
