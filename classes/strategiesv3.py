import random
import math

class Strategies():

    def __init__(self):
        self.number_of_strategies = 5
        self.strategies = []
        self.create_strategies()

    """create 5 stategies for each agent. Each strategy has a different memory and a weight to each element in the memory"""
    def create_strategies(self):
        for i in range(self.number_of_strategies):
            self.strategies.append([])
            self.memory = math.floor(random.random()*80 + 0.5)
            self.strategies[i].append(self.memory)
            self.strategies[i].append(self.setWeights(self.memory))

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

        return self.strategies[index][1]

    """With the current strategy and weight of each element in the strategy, estimate a new market value"""
    def nextPoint(self, weightList, setPoints):
        visionRange = len(weightList)

        if visionRange <= 1:
            return setPoints[-1]

        newpoint = setPoints[-visionRange]
        for i in reversed(range(visionRange)):
            b = (i + 1) * -1
            newpoint += weightList[i]*(setPoints[b] - setPoints[b-1])

        return newpoint

    def determine_best_strategies(self, marketprice, strategy_memory):
        None
        """
        Determines the deviation from the average market price for each of the strategies in the last strategy_memory cases
        and returns the strategy with the lowest total deviation to be picked in the future.
        Being closer to that price increases the chance of a match-up and minimises the losses.
        """
        #should return index of the best strategy
