import random
import math
import classes.properties as properties

class Strategies():

    def __init__(self, strategy_number):

        """number of strategies"""
        self.number_of_strategies = strategy_number

        """create a random memory size"""
        self.memory = math.floor(random.random()*80 + 1.)

        """create different strategies depending on the memory of the agent"""
        self.create_strategies(self.memory)

        self.strategy_evaluation_memory = properties.strategy_evaluation_memory

    """create stategies for each agent. Each strategy has a different memory and a weight to each element in the memory"""
    def create_strategies(self, memory):

        self.strategies = []
        self.memory = memory
        for i in range(self.number_of_strategies):
            self.strategies.append(self.set_weights(memory))

    """normalized weights"""
    def normalize_weights(self, weights):

        for i in range(len(weights)):
            weights[i] = weights[i]/sum(weights)*(len(weights) + 1)
        return weights

    """For each point in the memory, a weight is given"""
    def set_weights(self, vision_range):

        weight_list = []
        for i in range(vision_range):
            weight_list.append(random.random())
        self.normalize_weights(weight_list)
        return weight_list

    """With the current strategy and weight of each element in the strategy, estimate a new market value"""
    def next_point(self, weight_list, set_points):

        """to avoid index out of range errors, vision_range is set to the length of weight_list or the length of set_points, 
           depending on whatever has the smaller value. This allows it to theoretically run with less data than the memory can store"""
        vision_range = min(len(weight_list),len(set_points)-1)
        if vision_range < 1:
            return set_points[-1]

        newpoint = set_points[-vision_range - 1]
        weight_list = self.normalize_weights(weight_list[-vision_range:])
        for i in reversed(range(vision_range)):
            b = -(i + 1)
            newpoint += weight_list[b]*(set_points[b] - set_points[b-1])
			
        return newpoint
