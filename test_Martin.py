from classes.strategiesSellers import StrategiesSellers
import matplotlib.pyplot as plt

def main():
    
	history = []
	history_all = [8, 10]
	strat_sell = StrategiesSellers()
	print(strat_sell.sell_predict_last_2(history, history_all))
	
    
if __name__ == "__main__":
	main()