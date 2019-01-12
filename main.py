# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:42:36 2019

@author: Gebruiker
"""

from helpers.model import Model
import matplotlib.pyplot as plt

def main():
    
    modelA = Model()
    modelA.make_agents(10)
    modelA.run_simulation()

	plt.plot(modelA.stock_price_history)
	plt.show()
    
if __name__ == "__main__":
    main()