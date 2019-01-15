from classes.agent3 import Agent

def main():
	agent = Agent(True)
	agent.choose([10])
	print(agent.sell_prices)

if __name__ == "__main__":
    main()
