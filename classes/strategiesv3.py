import random
import math

class Strategies():

    def __init__(self, strategy_number):
        self.number_of_strategies = strategy_number
        self.strategies = []
        self.memory = math.floor(random.random()*80 + 1.)
        #self.memory = 40+1
        #evaluation memory is acutally one lower than the chard coded number. This should be fixed at some point
        self.strategy_evaluation_memory = 5
        #strategy_evaluation_memory can not exceed memory
        #self.memory = min(self.strategy_evaluation_memory, self.memory)
        self.create_strategies(self.memory)

    """create 5 stategies for each agent. Each strategy has a different memory and a weight to each element in the memory"""
    def create_strategies(self, memory):
        self.strategies = []
        self.memory = memory
        for i in range(self.number_of_strategies):
            self.strategies.append(self.setWeights(memory))

    def normalize_weights(self, weights):
        for i in range(len(weights)):
            weights[i] = weights[i]/sum(weights)*(len(weights) + 1)
        return weights

    """For each point in the memory, a weight is given"""
    def setWeights(self, visionRange):
        weightList = []
        for i in range(visionRange):
            weightList.append(random.random())
        self.normalize_weights(weightList)
        return weightList


    """With the current strategy and weight of each element in the strategy, estimate a new market value"""
    def nextPoint(self, weightList, setPoints):
        #to avoid index out of range errors, visionRange is set to the length of weightList or the length of setPoints, 
        #depending on whatever has the smaller value. This allows it to theoretically run with less data than the memory can store
        
        visionRange = min(len(weightList),len(setPoints)-1)
        if visionRange < 1:
            return setPoints[-1]

        newpoint = setPoints[-visionRange - 1]
        weightList = self.normalize_weights(weightList[-visionRange:])
        for i in reversed(range(visionRange)):
            b = -(i + 1)
            newpoint += weightList[b]*(setPoints[b] - setPoints[b-1])
			
        return newpoint


