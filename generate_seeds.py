import random
pricelist = [10]
for i in range(100):
	sell_price = pricelist[-1] + random.random() - 0.4
	pricelist.append(sell_price)
	print(pricelist[-1])


class Model():

    def __init__(self):
        self.time = 0
        self.end_time = 100
    
    def random_choose(self, stock_price_history):
        self.match_prices.append(0)
        self.strategy_index.append(0)
        if self.seller == True:
            sell_price = stock_price_history[-1] + random.random() - 0.4
            self.sell_prices.append(sell_price)
            return sell_price
        else:
            buy_price = stock_price_history[-1] + random.random() - 0.6
            self.buy_prices.append(buy_price)
            return buy_price