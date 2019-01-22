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
	
		self.memory = math.floor(random.random()*80 + 0.5)
		self.weights = self.setWeights(self.memory)

		self.match_prices = []
		self.profit = 0
		self.penalty = 0
		
	def update(self, winner, price):
		self.score_list.append(winner)
		if winner == True:
			self.score += 1
		else:
			self.score += -1
	
	def outcome(self, winner):
		if self.score == winner:
			self.score += 1
		self.score_list.append(self.score)
	
	def print_outcomes(self):
		print("The score list and history of this agent.")
		print(self.score_list)
		print(self.buy_price)
		print(self.sell_price)
		
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
	
	def setWeights(self, visionRange):
		weightList = []
		for i in range(visionRange - 1):
			weightList.append(random.random())
		for i in range(visionRange - 1):
			weightList[i] = weightList[i]/sum(weightList)*len(weightList)
			
		return weightList
	
	def nextPoint(self, weightList, setPoints):	
		visionRange = len(weightList)
		
		if visionRange <= 1:
			return setPoints[-1]
		
		newpoint = setPoints[-visionRange]
		for i in reversed(range(visionRange)):
			b = (i + 1) * -1
			newpoint += weightList[i]*(setPoints[b] - setPoints[b-1])
			
		return newpoint
	
	def choose(self, stock_price_history):
	
		#add for every turn a new 0
		self.match_prices.append(0)
		
		picksomething = self.nextPoint(self.weights, stock_price_history)
		self.sell_prices.append(picksomething)
		self.buy_prices.append(picksomething)
		return picksomething
		
	def matched(self, price):
		self.match_prices[-1] = price
		
	def calcProfit(self, marketprice):
		if self.match_prices[-1] == 0:
			self.profit += self.penalty
			return
		
		if len(self.match_prices) < 1:
			return
		
		if self.seller:
			self.profit += self.match_prices[-1] - marketprice
		else:
			self.profit += marketprice - self.match_prices[-1]