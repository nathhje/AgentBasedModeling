import csv

def make_csv(modelA):	
	print(len(modelA.sellers_list[0].strategy_index))
	print(len(modelA.sellers_list[-1].strategy_index))
	
	dataset = [["Price", "Time", "Id"]]
	for agent in modelA.sellers_list:
		for i in range(len(agent.sell_prices)):
			temp_list = [agent.sell_prices[i], i, agent.id]
			dataset.append(temp_list)
	
	#print(dataset)
	with open('data1.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerows(dataset)
	
	max_set = [True for i in range(len(modelA.sellers_list[-1].sell_prices))]
	min_set = [True for i in range(len(modelA.sellers_list[-1].sell_prices))]
	print(len(modelA.sellers_list[-1].sell_prices))
	for el in dataset[1:]:
		
		if max_set[el[1]]:
			max_set[el[1]] = el[0]
		elif max_set[el[1]] < el[0]:
			max_set[el[1]] = el[0]
			
		if min_set[el[1]]:
			min_set[el[1]] = el[0]
		elif min_set[el[1]] > el[0]:
			min_set[el[1]] = el[0]
	
	print(len(max_set), len(min_set), len(modelA.stock_price_history))	