# 1 Minute power


import io
import os
import json
import numpy

maxMinutePower = 0;

for filename in os.listdir('./data/rides/'):

	with open('./data/rides/' + filename, 'r') as file:
		rideDataDict = json.load(file);


	averageMinutes = []
	valIndex = 0

	dataLength = len(rideDataDict['watts_calc']);
	print dataLength

	for value in rideDataDict['watts_calc']:
		averagePower = 0;
		index = 60;
		while (index > 1):
			if (dataLength > (valIndex + index)):
				averagePower = averagePower + rideDataDict['watts_calc'][valIndex + index]
			index = index - 1;
		valIndex = valIndex + 1;
		averagePower = averagePower / 60
		averageMinutes.append(averagePower)



	# print averageMinutes;

	averagePower = 0
	minutesIndex = 0

	for minutePower in averageMinutes:
		averagePower = averagePower + minutePower;
		minutesIndex += 1

	minuteAverage = averagePower / minutesIndex;
	max = numpy.amax(averageMinutes)

	if max > maxMinutePower:
		maxMinutePower = max

print "Overall Max minute Power"
print maxMinutePower
