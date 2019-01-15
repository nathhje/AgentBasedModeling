# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:44:23 2019

@author: Gebruiker
"""

# agent - old agent file -- smartagent - new agent file
from classes.agent3 import Agent
import random

class Model():
    
	def __init__(self):
	
		self.time = 0
		self.end_time = 100
		self.matching_rounds = 10
		
		self.buyers_list = []
		self.sellers_list = []
		
		number_of_buyers = 10
		number_of_sellers = 10

		self.stock_price = 10
		self.stock_price_history = [10]
		
		self.temp_stock_price = 0
		
	def run_simulation(self):
		
		while(self.time < self.end_time):
			this_round = 0
			self.temp_stock_price = 0
			
			for buyer in self.buyers_list:
				buyer.choose(self.stock_price_history)
				
			for seller in self.sellers_list:
				seller.choose(self.stock_price_history)
				
			winning_agents = []
			temp_buyers = self.buyers_list.copy()
			temp_sellers = self.sellers_list.copy()
			
			for i in range(self.matching_rounds):
				
				winning_agents, temp_buyers, temp_sellers = self.match(winning_agents, temp_buyers, temp_sellers)
			
			
			if len(winning_agents) != 0:
				self.stock_price = 	self.temp_stock_price / (len(winning_agents) / 2)
			
			self.stock_price_history.append(self.stock_price)
			
			for buyer in self.buyers_list:
				if buyer in winning_agents:
					buyer.update(True, self.stock_price)
				else:
					buyer.update(False, self.stock_price)
			
			for seller in self.sellers_list:
				if seller in winning_agents:
					seller.update(True, self.stock_price)
				else:
					seller.update(False, self.stock_price)
			
			self.time += 1
			print(self.stock_price, this_round, [agent.stock_price for agent in self.sellers_list])
	
	def make_buyers(self, number_of_buyers):
		
		for i in range(number_of_buyers):
			self.buyers_list.append(Agent(False))
	
	def make_sellers(self, number_of_sellers):
	
		for i in range(number_of_sellers):
			self.sellers_list.append(Agent(True))
	
	def match(self, winning_agents, temp_buyers, temp_sellers):
	
		print([agent.buy_prices[-1] for agent in temp_buyers])
		winning_indices = []
		random.shuffle(temp_sellers)
		for i in range(len(temp_sellers)):
			if (temp_sellers[i].sell_prices[-1] < temp_buyers[i].buy_prices[-1]): 
				winning_indices.append(i)
				self.temp_stock_price += (temp_sellers[i].sell_prices[-1] + temp_buyers[i].buy_prices[-1]) / 2
		
		for i in sorted(winning_indices, reverse=True):
			winning_agents.append(temp_buyers[i])
			winning_agents.append(temp_sellers[i])
			del temp_buyers[i]
			del temp_sellers[i]
		
		return winning_agents, temp_buyers, temp_sellers
			
