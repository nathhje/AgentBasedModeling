# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:48:08 2019

@author: my favorite team
"""

import random
import math

class StrategiesBuyers():

    def __init__(self):
        self.threshold_low_price = 8
        self.threshold_high_price = 12
        self.n_time = 5
        self.market_memory = 3
        self.weights_dict = {0:0, 1:3, 2:1, 3:1}


    def buy_optimistic(self, history_self, history_all):
        """Agent tries to buy for 1 less than the market value last turn."""
        self.buy_price = history_all[-1] + 1
        return self.buy_price

    def buy_pesimistic(self, history_self, history_all):
        """Agent tries to buy for 1 more than the market value last turn."""
        self.buy_price = history_all[-1] - 1
        return self.buy_price

    def buy_predict_last_2(self, history_self, history_all):
        """Agent predicts the new buying price based on the progression
         of the last two steps. """
        print(self.n_time)
        if len(history_all) >= 2:
            self.buy_price = history_all[-1] + (history_all[-1]-history_all[-2])
        else:
            self.buy_price = history_all[-1]
        return self.buy_price

    def buy_predict_weighted_last_n(self, history_self, history_all):
        """Agent predicts the new buying price based on the progression 
        of the last n, n-1, n-2..., 2 steps. n is determined by the variable 
        self.market_memory and the length of history_all. The buying price 
        determined is a weighted average of the predicitons for the different lines.
        The weights are determined are stored in weights_dict. 
        """
        if self.market_memory >= len(history_all):
            max_length_of_line = len(history_all)
        else:
            max_length_of_line = self.market_memory
        sum_buy_price = 0
        sum_weights = 0
        for i in range(max_length_of_line):
            sum_buy_price += self.weights_dict[i] * (history_all[-1] + (history_all[-1]-history_all[-(i+1)]))
            sum_weights += self.weights_dict[i]
        self.buy_price = sum_buy_price/sum_weights
        return self.buy_price

"""Buyers strategies"""
"""
    #Agent buys if current price is below the threshold
    def buy_strat_below(self,history_self,history_all):
        if history_all[-1] < self.threshold_low_price:
            self.choice = 1
        else:
            self.choice = self.do_nothing_strat(history_self,history_all)
        return self.choice

    #Agent buys if after n times lowering the price, the price rices
    def buy_strat_after(self,history_self,history_all):
        self.choice = 1
        lowest_price = history_all[-self.n_time]
        for price in history_all[-self.n_time+1:-1]:
            if(lowest_price > price):
                lowest_price = price
            else:
                self.choice = 0
        return self.choice

    def buy_strat_hist_time(self,history_self,history_all):
        return self.choice
"""

