#!/usr/bin/python
import random


randList = []

maxnumber = 8614823636 - 10

whatweneed = 10000000

randList = [0] * (whatweneed * 4)
for i in range(whatweneed * 4):
	randList[i] = random.randint(0,maxnumber)


randList = sorted(randList)

uniqueRandList = [randList[0]]

for i in range(1 , len(randList)):
	if(randList[i] != randList[i-1]):
		uniqueRandList.append(randList[i])

random.shuffle(uniqueRandList)

uniqueRandList = uniqueRandList[:whatweneed]

for num in uniqueRandList:
	print num 
