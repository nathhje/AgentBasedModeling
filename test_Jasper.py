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
	for i in range(visionRange - 1):
		weightList[i] = weightList[i]/sum(weightList)*len(weightList)
		
	return weightList
	
def nextPoint(weightList, setPoints):
		
	visionRange = len(weightList)
	
	if visionRange <= 1:
		return setPoints[-1]
	
	newpoint = setPoints[-visionRange]
	for i in reversed(range(visionRange)):
		b = (i + 1) * -1
		print(b)
		newpoint += weightList[i]*(setPoints[b] - setPoints[b-1])
		
	return newpoint
		
		

for i in range(lengthPoints):
	setPoints.append(setPoints[-1] + random.random() - 0.5)
	

plt.figure()
plt.scatter(range(len(setPoints)), setPoints, c="black")
plt.scatter(len(setPoints), nextPoint(setWeights(1), setPoints), c="red", label="5")
plt.scatter(len(setPoints), nextPoint(setWeights(10), setPoints), c="green", label="10")
plt.scatter(len(setPoints), nextPoint(setWeights(15), setPoints), c="yellow", label="15")

plt.legend()
plt.show()

print(nextPoint(setWeights(visionRange), setPoints))


