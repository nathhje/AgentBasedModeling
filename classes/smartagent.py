# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:45:28 2019

@author: my favorite team
"""

import random
import math
from classes.strategies import Strategies

class Agent():
    
	def __init__(self):
		
		self.score = 0
		self.stock = math.floor(random.random()*2)
		
		self.score_list = []
		self.history = []
		
		self.strategies = Strategies()
		
	def choose(self, stock_price_history):
	
		if(self.stock > 0):
		
			if random.random() < 0.8:
				answer = self.strategies.sell_strat_above(self.score_list, stock_price_history)
			else: 
				answer = self.strategies.random_strat(self.score_list, stock_price_history, self.stock)
			
		elif self.stock == 0:
			if random.random() < 0.8:
				answer = self.strategies.buy_strat_below(self.score_list, stock_price_history)
				
			else: 
				answer = self.strategies.random_strat(self.score_list, stock_price_history, self.stock)
			
        
		self.stock += answer
		return answer
    
	def outcome(self, winner):
		
		if self.score == winner:
			
			self.score += 1
			
		self.score_list.append(self.score)
		
	def print_outcomes(self):
		print("The score list and history of this agent.")
		print(self.score_list)
		print(self.history)
