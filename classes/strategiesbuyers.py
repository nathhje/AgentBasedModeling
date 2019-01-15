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

    def buy_optimistic(self, history_self, history_all):
        """Agent tries to buy for 1 less than the market value last turn."""
        self.sell_price = history_all[-1] + 1
        return self.sell_price

    def buy_pesimistic(self, history_self, history_all):
        """Agent tries to sell for 1 more than the market value last turn."""
        self.sell_price = history_all[-1] - 1
        return self.sell_price

    def buy_predict_last_2(self, history_self, history_all):
        """Agent predicts the new selling price based on the progression
         of the last two steps. """
        print(self.n_time)
        if len(history_all) >= 2:
            self.sell_price = history_all[-1] + (history_all[-1]-history_all[-2])
        else:
            self.sell_price = history_all[-1]
        return self.sell_price



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

