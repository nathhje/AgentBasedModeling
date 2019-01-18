# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 09:42:36 2019

@author: Gebruiker
"""

from helpers.modelv4 import Model
import matplotlib.pyplot as plt

def main():

    modelA = Model()
    modelA.make_buyers()
    modelA.make_sellers()
    modelA.run_simulation()

    plt.figure()
    plt.plot(modelA.stock_price_history)
    plt.show()
    plt.savefig('results/stock_prices.png')

if __name__ == "__main__":
    main()
