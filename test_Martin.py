from classes.agent4 import Agent

def main():
	agent = Agent(True)
	price_history = [10.0, 11.0]
	agent.choose(price_history)
	#print(price_history)
	#print(agent.sell_prices)
	price_history.append(agent.sell_prices[-1])
	#print(price_history)
	agent.choose(price_history)
	#print(agent.sell_prices)
	price_history.append(agent.sell_prices[-1])
	print(price_history)
	print(price_history)
	
if __name__ == "__main__":
    main()

"""from classes.strategiessellers import StrategiesSellers
import matplotlib.pyplot as plt

def main():
    
	history = []
	history_all = [8, 10, 11, 10]
	strat_sell = StrategiesSellers()
	print(strat_sell.sell_predict_weighted_last_n(history, history_all))
	
    
if __name__ == "__main__":
	main()
"""