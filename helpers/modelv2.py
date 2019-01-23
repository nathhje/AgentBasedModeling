# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:44:23 2019

@author: Gebruiker
"""

# agent - old agent file -- smartagent - new agent file
from classes.smartagent import Agent

class Model():
    
	def __init__(self):
	
		self.time = 0
		self.end_time = 100
		self.agent_list = []
		self.winner_history = []
		self.stock_price = 10
		self.stock_price_history = [10]
		
		
	def run_simulation(self):
		
		while(self.time < self.end_time):
			this_round = 0
			for agent in self.agent_list:

				this_round += agent.choose(self.stock_price_history)
				
			if (this_round > 0):
				self.winner_history.append(True)
			else:
				self.winner_history.append(False)
		
			self.stock_price += self.stock_change(this_round)
			self.stock_price_history.append(self.stock_price)
		
			for agent in self.agent_list:
				agent.outcome(self.winner_history[-1])
				
			self.time += 1
			print(self.stock_price, this_round, [agent.stock for agent in self.agent_list])
	
	def make_agents(self, number_of_agents):
		
		for i in range(number_of_agents):
			self.agent_list.append(Agent())
	
	def stock_change(self, number_of_sells):
		return number_of_sells/2.0
