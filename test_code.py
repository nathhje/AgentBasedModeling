"""This will be a test file to test the code"""

from classes.agent3 import Agent

agent1 = Agent(True)
agent2 = Agent(False)

def test_seller():
	assert agent1.seller == True
	assert agent2.seller == False


