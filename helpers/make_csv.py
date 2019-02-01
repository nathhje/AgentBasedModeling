import csv

def make_csv(modelA):	
	
	dataset = [["Price", "Time", "Id", "Type", "Random", "Strategy", "StockPrice"]]
	for agent in modelA.sellers_list:
		for i in range(len(agent.sell_prices)):
			temp_list = [agent.sell_prices[i], i, agent.id, "sell", agent.random, agent.strategy_index[i]]
			dataset.append(temp_list)
	for agent in modelA.buyers_list:
		for i in range(len(agent.buy_prices)):
			temp_list = [agent.buy_prices[i], i, agent.id, "buy", agent.random, agent.strategy_index[i], modelA.stock_price_history[i + modelA.warming_up_time]]
			dataset.append(temp_list)
	
	with open('data1.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(dataset)
	
	max_set_sell = [True for i in range(len(modelA.sellers_list[-1].sell_prices))]
	min_set_sell = [True for i in range(len(modelA.sellers_list[-1].sell_prices))]
	max_set_buy = [True for i in range(len(modelA.buyers_list[-1].buy_prices))]
	min_set_buy = [True for i in range(len(modelA.buyers_list[-1].buy_prices))]

	for el in dataset[1:]:
		if el[3] == "sell":
			if max_set_sell[el[1]] == True:
				max_set_sell[el[1]] = el[0]
			elif max_set_sell[el[1]] < el[0]:
				max_set_sell[el[1]] = el[0]
				
			if min_set_sell[el[1]] == True:
				min_set_sell[el[1]] = el[0]
			elif min_set_sell[el[1]] > el[0]:
				min_set_sell[el[1]] = el[0]
		else:
			if max_set_buy[el[1]] == True:
				max_set_buy[el[1]] = el[0]
			elif max_set_buy[el[1]] < el[0]:
				max_set_buy[el[1]] = el[0]
				
			if min_set_buy[el[1]] == True:
				min_set_buy[el[1]] = el[0]
			elif min_set_buy[el[1]] > el[0]:
				min_set_buy[el[1]] = el[0]
			
	max_set_sell = modelA.stock_price_history[:modelA.warming_up_time + 1] + max_set_sell
	min_set_sell = modelA.stock_price_history[:modelA.warming_up_time + 1] + min_set_sell
	max_set_buy = modelA.stock_price_history[:modelA.warming_up_time + 1] + max_set_buy
	min_set_buy = modelA.stock_price_history[:modelA.warming_up_time + 1] + min_set_buy
	
	total = [["Time", "Stockprice", "Maxsell", "Minsell", "Maxbuy", "Minbuy"]]
	for i in range(len(modelA.stock_price_history)):
		total.append([i, modelA.stock_price_history[i], max_set_sell[i], min_set_sell[i], max_set_buy[i], min_set_buy[i]])
	
	with open('data2.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(total)