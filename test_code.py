"""This will be a test file to test the code"""

from classes.agentv7 import Agent

agent1 = Agent(True,1,1,False)
agent2 = Agent(False,1,1,False)

def test_seller():
	assert agent1.seller == True
	assert agent2.seller == False


