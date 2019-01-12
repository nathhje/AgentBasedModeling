# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:44:23 2019

@author: Gebruiker
"""

from classes.agent import Agent

class Model():
    
	def __init__(self):
	
		self.time = 0
		self.end_time = 100
		self.agent_list = []
		self.winner_history = []
		
	def run_simulation(self):
		
		while(self.time < self.end_time):
			this_round = 0
			for agent in self.agent_list:
				if agent.choose():
					this_round += 1
				
			if (this_round > len(self.agent_list) / 2):
				self.winner_history.append(True)
			else:
				self.winner_history.append(False)
		
			for agent in self.agent_list:
				agent.outcome(self.winner_history[-1])
				
			self.time += 1
	
	def make_agents(self, number_of_agents):
		
		for i in range(number_of_agents):
			self.agent_list.append(Agent())
	
