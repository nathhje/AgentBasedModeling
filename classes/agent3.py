# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:45:28 2019

@author: my favorite team
"""

import random
import math
import numpy as np
from classes.strategiesbuyers import StrategiesBuyers
from classes.strategiessellers import StrategiesSellers

class Agent():
    
	def __init__(self, seller):
		
		self.score = 0
		self.score_list = []

		self.seller = seller	
		self.buy_prices = []
		self.sell_prices = []
		
		self.buy_strategies = StrategiesBuyers()
		self.sell_strategies = StrategiesSellers()
		
	def choose(self, stock_price_history):

		
		if self.seller == True:
		
			#LINES UNDERNEATH IS TEMP FIX
			sell_price = stock_price_history[-1] + random.random() - 0.4
			self.sell_prices.append(sell_price)
			return sell_price
			
			"""choose between sell strategies"""
			sell_price = self.sell_strategies.sell_optimistic(0,stock_price_history)
			self.sell_prices.append(sell_price)
	
		else:
		
			#LINES UNDERNEATH IS TEMP FIX
			buy_price = stock_price_history[-1] + random.random() - 0.6
			self.buy_prices.append(buy_price)
			return buy_price
			
			"""choose between buy strategies"""
			buy_price = self.buy_strategies.buy_optimistic(0,stock_price_history)
			self.buy_prices.append(buy_price)

	def update(self, winner):
		self.score_list.append(winner)
		if winner == True:
			self.score += 1
		else:
			self.score += -1

	def print_outcomes(self):
		print("The score list and history of this agent.")
		print(self.score_list)
		print(self.buy_price)
		print(self.sell_price)
		
	def update(self, bool, price):
		pass
