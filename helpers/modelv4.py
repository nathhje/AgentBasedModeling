# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:44:23 2019

@author: Gebruiker
"""

# agent - old agent file -- smartagent - new agent file
from classes.agentv7 import Agent
import random
import math

class Model():

    def __init__(self, random_agent):

        self.time = 0
        self.end_time = 100

        self.buyers_list = []
        self.sellers_list = []

        self.number_of_buyers = 100
        self.number_of_sellers = 100
        self.ratio_of_random_agents = random_agent
		
        self.stock_price_history = [10]
        self.temp_stock_price = 0

        # Warming-up parameters
        self.warm_up_type = [0,0]
        self.warming_up_time = 50
        self.number_of_wu_agents = 10
        self.warm_up_buyers_list = []
        self.warm_up_sellers_list = []

        #Parameters for plotting notes Jasper
        self.notes_prices_time_sellers = []
        self.notes_prices_time_buyers = []
        self.notes_prices_sell = []
        self.notes_prices_buy = []
        self.notes_prices_match = []
        self.notes_prices_time_match = []
		
        self.id_counter = 0

    """
    Make the Agents buyers and sellers
    Buyers are False, sellers are True
    """
    def make_buyers(self,strategy_number):
        for i in range(self.number_of_buyers):
            self.buyers_list.append(Agent(False, self.id_counter, strategy_number))
            self.id_counter += 1

    def make_sellers(self,strategy_number):
        for i in range(self.number_of_sellers):
            self.sellers_list.append(Agent(True, self.id_counter, strategy_number))
            self.id_counter += 1

    """Start warming up and running the simulation"""
    def warm_up(self):
        for i in range(self.number_of_wu_agents):
            self.warm_up_buyers_list.append(Agent(False, self.id_counter,1))
            self.warm_up_sellers_list.append(Agent(True, self.id_counter,1))

		#Warming up period
        while(self.time < self.warming_up_time):
            for i in range(self.number_of_wu_agents):
                self.warm_up_buyers_list[i].random_choose(self.stock_price_history)
                self.warm_up_sellers_list[i].random_choose(self.stock_price_history)

            winning_agents = []
            temp_buyers =  self.warm_up_buyers_list.copy()
            temp_sellers = self.warm_up_sellers_list.copy()

            #Match the buyers and sellers
            winning_agents, temp_buyers, temp_sellers = self.match(winning_agents, temp_buyers, temp_sellers)

            #Update the stock price based on the match
            if self.time <= self.warming_up_time / 2.0:
                self.temp_stock_price = (self.temp_stock_price / (len(winning_agents) / 2)) + random.random()/10*self.warm_up_type[0]
            else:
                self.temp_stock_price = (self.temp_stock_price / (len(winning_agents) / 2)) + random.random()/10*self.warm_up_type[1]
            
            #self.temp_stock_price = (self.temp_stock_price / (len(winning_agents) / 2))
            self.stock_price_history.append(self.temp_stock_price)

            self.temp_stock_price = 0
            self.time += 1

    def run_simulation(self):
        self.warm_up()
        #for i in range(90):
        #    self.time += 1
        #    #self.stock_price_history.append(self.stock_price_history[-1] + 0.05 )
        #    self.stock_price_history.append(self.stock_price_history[-1] + 2 * math.sin(i * math.pi / 17))
        

        #Start the real simulation
        
        for buyer in self.buyers_list:
            buyer.initial_track_strategies(self.stock_price_history)
        for seller in self.sellers_list:
            seller.initial_track_strategies(self.stock_price_history)

        while(self.time < self.end_time + self.warming_up_time):
            for buyer in self.buyers_list[int(round((self.ratio_of_random_agents*self.number_of_buyers))):]:
                buyer.match_prices.append(0)
                buyer.track_strategies(self.stock_price_history)
                buyer.buy_prices.append(buyer.choose(self.stock_price_history, buyer.choose_strategy()))
            for buyer in self.buyers_list[:int(round((self.ratio_of_random_agents*self.number_of_buyers)))]:
                buyer.random_choose(self.stock_price_history)

            for seller in self.sellers_list[int(round(self.ratio_of_random_agents*self.number_of_sellers)):]:
                seller.match_prices.append(0)
                seller.track_strategies(self.stock_price_history)
                seller.sell_prices.append(seller.choose(self.stock_price_history, seller.choose_strategy()))
            for seller in self.sellers_list[:int(round(self.ratio_of_random_agents*self.number_of_sellers))]:
                seller.random_choose(self.stock_price_history)

            winning_agents = []
            temp_buyers = self.buyers_list.copy()
            temp_sellers = self.sellers_list.copy()

            #Match the buyers and sellers
            winning_agents, temp_buyers, temp_sellers = self.match(winning_agents, temp_buyers, temp_sellers)

            #Update the stock price based on the match
            self.temp_stock_price = self.temp_stock_price / (len(winning_agents) / 2)
            self.stock_price_history.append(self.temp_stock_price)

            self.temp_stock_price = 0
            self.time += 1

            #Calculate the profit of the agents
            for buyer in self.buyers_list:
                buyer.calcProfit(self.stock_price_history[-1])
            for seller in self.sellers_list:
                seller.calcProfit(self.stock_price_history[-1])
                #print(seller.profit)
        #for buyer in self.buyers_list:
        #    print(buyer.id, buyer.profit)
        #for seller in self.sellers_list:
        #    print(seller.id, seller.profit)

    """Match the Agents buyers and sellers"""
    #Match the Agents buyers and sellers
    def match(self, winning_agents, temp_buyers, temp_sellers):
        #Notes of the prices of sellers and buyers
        for i in range(len(temp_sellers)):
            self.notes_prices_time_sellers.append(self.time)
            self.notes_prices_sell.append(temp_sellers[i].sell_prices[-1])

        for j in range(len(temp_buyers)):
            self.notes_prices_time_buyers.append(self.time)
            self.notes_prices_buy.append(temp_buyers[j].buy_prices[-1])

        #Starting parameters, winning is a match
        winning_indices = []
        random.shuffle(temp_sellers)
        random.shuffle(temp_buyers)

        for i in range(len(temp_sellers)):
            for j in range(len(temp_buyers)):
                if temp_sellers[i].sell_prices[-1] <= temp_buyers[j].buy_prices[-1]:
                    winning_indices.append(i)

                    average_price = (temp_sellers[i].sell_prices[-1] + temp_buyers[j].buy_prices[-1]) / 2
                    temp_sellers[i].matched(average_price)
                    temp_buyers[j].matched(average_price)
                    self.temp_stock_price += average_price

                    #Notes of the prices of matches
                    self.notes_prices_match.append(temp_sellers[i].sell_prices[-1])
                    self.notes_prices_match.append(temp_buyers[j].buy_prices[-1])
                    self.notes_prices_time_match.append(self.time)  #For the matched seller
                    self.notes_prices_time_match.append(self.time) #For the matched buyer

                    #Append the matching buyers to the winning agents
                    #And delete those from the temporary list
                    winning_agents.append(temp_buyers[j])
                    del temp_buyers[j]
                    break

        #Append the matching sellers to the winning agents
        #And delete those from the temporary list
        for i in sorted(winning_indices, reverse=True):
            winning_agents.append(temp_sellers[i])
            del temp_sellers[i]

        return winning_agents, temp_buyers, temp_sellers
        
