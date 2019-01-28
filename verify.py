import random
import matplotlib.pyplot as plt

"""For each point in the memory, a weight is given"""
def setWeights(visionRange):
    weightList = []
    for i in range(visionRange - 1):
        weightList.append(random.random())
    normalize_weights(weightList)
    return weightList


"""With the current strategy and weight of each element in the strategy, estimate a new market value"""
def nextPoint(weightList, setPoints):
    #to avoid index out of range errors, visionRange is set to the length of weightList or the length of setPoints, 
    #depending on whatever has the smaller value. This allows it to theoretically run with less data than the memory can store
    #print(weightList, setPoints)
    visionRange = min(len(weightList),len(setPoints)-1)
    if visionRange < 1:
        return setPoints[-1]

    newpoint = setPoints[-visionRange - 1]
    for i in reversed(range(visionRange)):
        b = -(i + 1)
        newpoint += weightList[b]*(setPoints[b] - setPoints[b-1])
		
    return newpoint
	
def normalize_weights(weights):
    sumW = sum(weights)
    lenW = len(weights)
    for i in range(len(weights)):
        weights[i] = weights[i]/sumW*(lenW + 1)
    return weights

set_points = []
for i in range(10):
	set_points.append(0.5 * i ** 2)
results = []

plt.figure()
plt.scatter(range(len(set_points)), set_points, c="black")
plt.scatter(len(set_points), nextPoint([1 + 1./2 for i in range(8)], set_points))
for i in range(20):
	plt.scatter(len(set_points), nextPoint(setWeights(8), set_points))
plt.legend()
plt.show()

