import random
import numpy as np
import matplotlib.pyplot as plt

lengthPoints = 20
visionRange = 5
startValue = 10

setPoints = [startValue]

def setWeights(visionRange):
	weightList = []
	for i in range(visionRange - 1):
		weightList.append(random.random())
	sumW = sum(weightList)
	lenW = len(weightList)
	for i in range(visionRange - 1):
		weightList[i] = weightList[i]/sumW*lenW
		
	return weightList
	
def nextPoint(weightList, setPoints):
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
		
		

for i in range(lengthPoints):
	setPoints.append(setPoints[-1] + 0.1)
	
specialWeights = [1 for i in range(15)]

print(setWeights(5))

plt.figure()
plt.scatter(range(len(setPoints)), setPoints, c="black")
#plt.scatter(len(setPoints), nextPoint(setWeights(1), setPoints), c="red", label="5")
#plt.scatter(len(setPoints), nextPoint(setWeights(10), setPoints), c="green", label="10")
for i in range(100):
    plt.scatter(len(setPoints), nextPoint(setWeights(3), setPoints), c="yellow", label="15")
plt.scatter(len(setPoints), nextPoint(specialWeights, setPoints), c="purple", label="average")
plt.legend()
plt.show()

print(nextPoint(setWeights(visionRange), setPoints))


