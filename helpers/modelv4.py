# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:44:23 2019

@author: Gebruiker
"""

# agent - old agent file -- smartagent - new agent file
from classes.secretAgent import Agent
import random

class Model():

    def __init__(self):

        self.time = 0
        self.end_time = 500
        self.matching_rounds = 10

        self.buyers_list = []
        self.sellers_list = []

        self.number_of_buyers = 200
        self.number_of_sellers = 200

        self.stock_price = 10
        self.stock_price_history = [10]

        self.temp_stock_price = 0
		
        # Warming-up parameters
        self.warming_up_time = 100
        self.number_of_wo_agents = 10
        self.warm_up_buyers_list = []
        self.warm_up_sellers_list = []
		
        #Jasper
        self.notes_prices_time = []
        self.notes_prices_sell = []
        self.notes_prices_buy = []
        self.notes_prices_match = []
        self.notes_prices_time_match = []
		
    def run_simulation(self):
		
        for i in range(self.number_of_wo_agents):
            self.warm_up_buyers_list.append(Agent(False))
            self.warm_up_sellers_list.append(Agent(True))
		
		#Warming up period
        while(self.time < self.warming_up_time):
            for i in range(self.number_of_wo_agents):
                self.warm_up_buyers_list[i].random_choose(self.stock_price_history)
                self.warm_up_sellers_list[i].random_choose(self.stock_price_history)
				
            winning_agents = []
            temp_buyers =  self.warm_up_buyers_list.copy()
            temp_sellers = self.warm_up_sellers_list.copy()

            winning_agents, temp_buyers, temp_sellers = self.match(winning_agents, temp_buyers, temp_sellers)

            self.stock_price = self.temp_stock_price / (len(winning_agents) / 2)
            self.temp_stock_price = 0
            self.stock_price_history.append(self.stock_price)

            self.time += 1

			
        while(self.time < self.end_time + self.warming_up_time):

            for buyer in self.buyers_list:
                buyer.choose(self.stock_price_history)

            for seller in self.sellers_list:
                seller.choose(self.stock_price_history)
				
            #print([[agent.buy_prices[-1], agent.memory] for agent in temp_buyers])

            winning_agents = []
            temp_buyers = self.buyers_list.copy()
            temp_sellers = self.sellers_list.copy()

            winning_agents, temp_buyers, temp_sellers = self.match(winning_agents, temp_buyers, temp_sellers)

            self.stock_price = self.temp_stock_price / (len(winning_agents) / 2)
            self.temp_stock_price = 0
            self.stock_price_history.append(self.stock_price)

            for buyer in self.buyers_list:
                if buyer in winning_agents:
                    buyer.update(True)#, self.stock_price)
                else:
                    buyer.update(False)#, self.stock_price)

            for seller in self.sellers_list:
                if seller in winning_agents:
                    seller.update(True)#, self.stock_price)
                else:
                    seller.update(False)#, self.stock_price)

            self.time += 1
			
            for buyer in self.buyers_list:
                buyer.calcProfit(self.stock_price_history[-1])

            for seller in self.sellers_list:
                seller.calcProfit(self.stock_price_history[-1])			
			
            


    def make_buyers(self):
        for i in range(self.number_of_buyers):
            self.buyers_list.append(Agent(False))

    def make_sellers(self):
        for i in range(self.number_of_sellers):
            self.sellers_list.append(Agent(True))


    def define_lists(self, temp_buyers, temp_sellers):
        shortest_list = temp_sellers
        longest_list = temp_buyers
        if (len(temp_buyers) < len(temp_sellers)):
            shortest_list = temp_buyers
            longest_list = temp_sellers
        return shortest_list, longest_list


    def match(self, winning_agents, temp_buyers, temp_sellers):

        shortest_list, longest_list = self.define_lists(temp_buyers, temp_sellers)
        for i in range(len(temp_sellers)):
            self.notes_prices_time.append(self.time)
            self.notes_prices_sell.append(temp_sellers[i].sell_prices[-1])
            self.notes_prices_buy.append(temp_buyers[i].buy_prices[-1])

			
        #print("shortest",shortest_list)
        #print("longest",longest_list)
        #print("sell",temp_sellers)
        #print("buy",temp_buyers)

        winning_indices = []
        random.shuffle(temp_sellers)
        random.shuffle(temp_buyers)
        for i in range(len(shortest_list)):
            if (temp_sellers[i].sell_prices[-1] <= temp_buyers[i].buy_prices[-1]):
                winning_indices.append(i)
                
                temp_sellers[i].matched((temp_sellers[i].sell_prices[-1] + temp_buyers[i].buy_prices[-1]) / 2)
                temp_buyers[i].matched((temp_sellers[i].sell_prices[-1] + temp_buyers[i].buy_prices[-1]) / 2)
                self.temp_stock_price += (temp_sellers[i].sell_prices[-1] + temp_buyers[i].buy_prices[-1]) / 2
                
                self.notes_prices_match.append(temp_sellers[i].sell_prices[-1])
                self.notes_prices_match.append(temp_buyers[i].buy_prices[-1])
                self.notes_prices_time_match.append(self.time)
                self.notes_prices_time_match.append(self.time)

        for i in sorted(winning_indices, reverse=True):
            winning_agents.append(temp_buyers[i])
            winning_agents.append(temp_sellers[i])
            del temp_buyers[i]
            del temp_sellers[i]

        winning_indices = []

        for i in range(len(temp_sellers)):
            for j in range(len(temp_buyers)):
                if temp_sellers[i].sell_prices[-1] <= temp_buyers[j].buy_prices[-1]:
                    winning_indices.append(i)
                    self.temp_stock_price += (temp_sellers[i].sell_prices[-1] + temp_buyers[j].buy_prices[-1]) / 2
                    self.notes_prices_match.append(temp_sellers[i].sell_prices[-1])
                    self.notes_prices_match.append(temp_buyers[j].buy_prices[-1])
                    self.notes_prices_time_match.append(self.time)
                    self.notes_prices_time_match.append(self.time)
                    winning_agents.append(temp_buyers[j])
                    del temp_buyers[j]
                    break

        for i in sorted(winning_indices, reverse=True):
			
            winning_agents.append(temp_sellers[i])
            del temp_sellers[i]
			


        return winning_agents, temp_buyers, temp_sellers

    def match2(self, winning_agents, temp_buyers, temp_sellers):

        shortest_list, longest_list = self.define_lists(temp_buyers, temp_sellers)
        len_shortest_list = len(shortest_list)+1
        #Base case
        #OR WHILE STATEMENT. To match the buyers and sellers,
        #

        while len_shortest_list != len(shortest_list):
            only_once = 0
            len_shortest_list = len(shortest_list)

            winning_indices = []
            random.shuffle(temp_sellers)
            random.shuffle(temp_buyers)
            for i in range(len(shortest_list)):
                if only_once == 0:
                    print(temp_sellers[i].sell_prices[-1],temp_buyers[i].buy_prices[-1])
                if (temp_sellers[i].sell_prices[-1] <= temp_buyers[i].buy_prices[-1]):
                    winning_indices.append(i)
                    self.temp_stock_price += (temp_sellers[i].sell_prices[-1] + temp_buyers[i].buy_prices[-1]) / 2

            for i in sorted(winning_indices, reverse=True):
                winning_agents.append(temp_buyers[i])
                winning_agents.append(temp_sellers[i])
                del temp_buyers[i]
                del temp_sellers[i]

            shortest_list, longest_list = self.define_lists(temp_buyers, temp_sellers)
            only_once = 1

        return winning_agents, temp_buyers, temp_sellers
