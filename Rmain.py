# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:42:36 2019

@author: Gebruiker
"""

from helpers.modelv4 import Model
from helpers.make_csv import make_csv
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import classes.properties as properties

def main():

	perc = [1, 10, 50]
	plt.figure()
	plt.title("The effect of memory on profit per agent")
	
	zlist = [10]
	for i in range(90):
		zlist.append(zlist[-1] + 0.1)
	
	saveithere = [[],[]]
	for q in range(0, 80, 10):
	
		
		
		for j in range(10):
			
			random.seed(j*random.random()*1111)
			modelA = Model(0.5)
			modelA.make_buyers(properties.agent_memory)
			modelA.make_sellers(properties.agent_memory)
			
			for agent in modelA.buyers_list:
				agent.strategies.memory = q
				agent.strategies.create_strategies(agent.strategies.memory)
			
			for agent in modelA.sellers_list:
				agent.strategies.memory = q
				agent.strategies.create_strategies(agent.strategies.memory)
			
			#for i in range(90):
			#	modelA.stock_price_history.append(zlist[i])
			#modelA.time = 91
			modelA.warm_up()
			modelA.run_simulation()
			
			#print(modelA.buyers_list[-1].strategy_index)
			##Plot normal stockflow
			
			#plt.plot(modelA.stock_price_history)
			#plt.show()
			#plt.savefig('results/stock_prices.png')
			
			##Plot correlation
			#list1, list2 = [], []
			#for agent in modelA.buyers_list:
			#    list1.append(agent.profit)
			#    list2.append(agent.memory)
			#list3, list4 = [], []
			#for agent in modelA.sellers_list:
			#    list3.append(agent.profit)
			#    list4.append(agent.memory)
			#print(modelA.time)
			#
			#
			#plt.scatter(list2, list1, c="blue")
			#plt.scatter(list4, list3, c="green")
			#plt.ylabel("Profit")
			#plt.xlabel("Memory")
			#plt.show()
			#plt.savefig('results/crossreverence.png')
			
			#Plot matches 
			
			"""create plots"""
			#plt.scatter(modelA.plots_prices_time_sellers, modelA.plots_prices_sell, s=3, c="blue")
			#plt.scatter(modelA.plots_prices_time_buyers, modelA.plots_prices_buy, s=3, c="green")
			#plt.scatter(modelA.plots_prices_time_match, modelA.plots_prices_match, s=3, c="orange")
			meanmemory = 0
			counter = 0
			for agent in modelA.buyers_list:
				if not agent.random:
					meanmemory += agent.strategies.memory
					counter += 1
					#saveithere[0].append(agent.profit)
			saveithere[0].append(meanmemory/counter)
			saveithere[1].append(np.std(modelA.stock_price_history[100:]))
			print(q, j)
		
		##print(saveithere)
		#meanlist = []
		#stdlist = []
		#for list in saveithere:
		#	#plt.plot(range(len(modelA.stock_price_history)), list, c="grey")
		#	meanlist.append(np.mean(list[90:])/len(list[90:]))
		#	stdlist.append(np.std([j-i for i, j in zip(list[90:][:-1], list[90:][1:])]))
		##plt.plot(range(len(modelA.stock_price_history))[0:90], list[0:90], c="red")
		##plt.title("Linear warming-up period with 10% random agents")
		##plt.axis(ymin = 0)
		##plt.xlabel("Timesteps")
		##plt.ylabel("Artifical stockprice")
		#print("Hier")
		##plt.show()
		##plt.savefig('results/stock_prices.png')
		#print(np.mean(list[:90])/len(list[:90]))
		#print(np.std([j-i for i, j in zip(list[:90][:-1], list[:90][1:])]))
		#print(meanlist)
		#print(stdlist)
	
		#plt.subplot(3,2,(1 + q * 2))
		#plt.hist(meanlist, normed=True)
		#plt.axvline(np.mean(list[:90])/len(list[:90]), color='red', linestyle='dashed', linewidth=1)
		#if q==0:
		#	plt.title("Average growth")
		#plt.xlabel("Average growth in model with "  + str(perc[q]) + "% random agents")
		##plt.xlim(-0.1, 0.2)
		#plt.ylabel("Frequency")
		#
		#plt.subplot(3,2,(2 + q * 2))
		#plt.hist(stdlist, normed=True)
		#plt.axvline(np.std([j-i for i, j in zip(list[:90][:-1], list[:90][1:])]), color='red', linestyle='dashed', linewidth=1)
		#if q==0:
		#	plt.title("Average standard deviation")
		#plt.xlabel("Average standard deviation of of change with "  + str(perc[q]) + "% random agents")
		#plt.ylabel("Frequency")
		
	plt.figure()
	plt.scatter(saveithere[0], saveithere[1])
	plt.xlabel("Memory")
	plt.ylabel("Variance in the market")
	plt.show()
	
	
	#make_csv(modelA)
	

	
if __name__ == "__main__":
    main()
