# 20 Minute power


import io
import json
import numpy

with open('./data/rideData.json', 'r') as file:
	rideDataDict = json.load(file);


averageTwentyMinutes = []
valIndex = 0

dataLength = len(rideDataDict['watts_calc']);

for value in rideDataDict['watts_calc']:
	averagePower = 0;
	index = 1200;
	while (index > 1):
		if (dataLength > (valIndex + index)):
			averagePower = averagePower + rideDataDict['watts_calc'][valIndex + index]
		index = index - 1;
	valIndex = valIndex + 1;
	averagePower = averagePower / 1200
	averageTwentyMinutes.append(averagePower)



# print averageMinutes;

averagePower = 0
twentyMinutesIndex = 0

for twentyMinutePower in averageTwentyMinutes:
	averagePower = averagePower + twentyMinutePower;
	twentyMinutesIndex += 1

twentyMinuteAverage = averagePower / twentyMinutesIndex;

print "Average 20 Minute Power"
print twentyMinuteAverage;

print "Max 20 Minute Power"
print numpy.amax(averageTwentyMinutes)