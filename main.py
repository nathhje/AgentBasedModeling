# -*- coding: utf-8 -*-
"""
The main file of the stock market ABM model. By running this file the model will
be run once with standard input and a plot will be made that shows the offers at
each time step. Blue is sellers that were unable to sell, green is buyers that
were unable to buy, orange are agents that managed to make a match and red is
the stock price.
"""

from helpers.modelv4 import Model
import matplotlib.pyplot as plt
import classes.properties as properties

def main():

    """initialise and run model"""
    modelA = Model(properties.ratio_of_random_agents)
    modelA.make_buyers(properties.agent_memory)
    modelA.make_sellers(properties.agent_memory)
    modelA.warm_up()
    modelA.run_simulation()

    plt.figure()

    """create plots"""
    plt.scatter(modelA.plots_prices_time_sellers, modelA.plots_prices_sell, s=3, c="blue")
    plt.scatter(modelA.plots_prices_time_buyers, modelA.plots_prices_buy, s=3, c="green")
    plt.scatter(modelA.plots_prices_time_match, modelA.plots_prices_match, s=3, c="orange")
    plt.plot(range(len(modelA.stock_price_history)), modelA.stock_price_history, c="red")
    plt.axis(ymin = 0)
    plt.show()
    
if __name__ == "__main__":
    main()
