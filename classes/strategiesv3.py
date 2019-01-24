import random
import math

class Strategies():

    def __init__(self):
        self.number_of_strategies = 3
        self.strategies = []
        self.memory = math.floor(random.random()*80 + 1.)
        self.memory = 5+1
        self.create_strategies(self.memory)

    """create 5 stategies for each agent. Each strategy has a different memory and a weight to each element in the memory"""
    def create_strategies(self, memory):
        for i in range(self.number_of_strategies):
            self.strategies.append(self.setWeights(memory))

    """For each point in the memory, a weight is given"""
    def setWeights(self, visionRange):
        weightList = []
        for i in range(visionRange - 1):
            weightList.append(random.random())
        for i in range(visionRange - 1):
            weightList[i] = weightList[i]/sum(weightList)*len(weightList)

        return weightList

    """pick one of the strategies (randomly)"""
    def choose_strategy(self):
        #random strategy
        index = math.floor(random.random()*len(self.strategies))
        #calculated best strategy
        #index = determine_best_strategies(marketprice, strategy_memory)
        return self.strategies[index]

    """With the current strategy and weight of each element in the strategy, estimate a new market value"""
    def nextPoint(self, weightList, setPoints):
        #to avoid index out of range errors, visionRange is set to the length of weightList or the length of setPoints, 
        #depending on whatever has the smaller value. This allows it to theoretically run with less data than the memory can store
        visionRange = min(len(weightList),len(setPoints)-1)
        if visionRange <= 1:
            return setPoints[-1]

        newpoint = setPoints[-visionRange]
        for i in reversed(range(visionRange)):
            b = -(i + 1)
            newpoint += weightList[b]*(setPoints[b] - setPoints[b-1])

        return newpoint

    def determine_best_strategies(self, marketprice, strategy_memory):
        None
        """
        Determines the deviation from the average market price for each of the strategies in the last strategy_memory cases
        and returns the strategy with the lowest total deviation to be picked in the future.
        Being closer to that price increases the chance of a match-up and minimises the losses.
        """
        #should return index of the best strategy


