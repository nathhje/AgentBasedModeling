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
        self.n_time = 5

    """"Basic strategies""" #With old boolean
    def random_strat(self,history_self,history_all, stock):
        self.choice = math.floor(random.random()*2)
        if stock > 0:
            self.choice *= -1
        return self.choice

    """Choice: -1 sell, 0 do nothing, 1 buy"""
    #self.history.append(self.choice) add this to agent!
    def do_nothing_strat(self, history_self, history_all):
        self.choice = 0
        return self.choice

    """Buyers strategies"""
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


    """Sellers strategies"""
    #Agent sell if current price is above the threshold
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
