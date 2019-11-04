
import io
import os
import json
import numpy
import argparse
import sys
import imp

constants = imp.load_source('data.constants', './data/data.py')

parser = argparse.ArgumentParser(description='Get Max power for a given time period')
parser.add_argument('-t', metavar='t', type=int,
                    help='The duration in seconds for which you wish to find the max power')


args = parser.parse_args()

# Should only run if coming from command line with argument
if (args.t):
	time = args.t
	maxPower = 0;

	for filename in os.listdir('./data/rides/'):

		with open('./data/rides/' + filename, 'r') as file:
			rideDataDict = json.load(file);


		averages = []
		valIndex = 0

		dataLength = len(rideDataDict['watts_calc']);

		for value in rideDataDict['watts_calc']:
			averagePower = 0;
			index = time;
			while (index > 1):
				if (dataLength > (valIndex + index)):
					averagePower = averagePower + rideDataDict['watts_calc'][valIndex + index]
				index = index - 1;
			valIndex = valIndex + 1;
			averagePower = averagePower / time
			averages.append(averagePower)

		averagePower = 0
		timeIndex = 0

		for power in averages:
			averagePower = averagePower + power;
			timeIndex += 1

		timeAverage = averagePower / timeIndex;
		max = numpy.amax(averages)

		if max > maxPower:
			maxPower = max

	print("Max Power for " + str(time) + " seconds")
	print(maxPower)
	print( str(maxPower / constants.weight) + " W/Kg" )


def getMaxPower(time): 
	maxPower = 0;

	for filename in os.listdir('./data/rides/'):

		with open('./data/rides/' + filename, 'r') as file:
			rideDataDict = json.load(file);


		averages = []
		valIndex = 0

		dataLength = len(rideDataDict['watts_calc']);

		for value in rideDataDict['watts_calc']:
			averagePower = 0;
			index = time;
			while (index > 1):
				if (dataLength > (valIndex + index)):
					averagePower = averagePower + rideDataDict['watts_calc'][valIndex + index]
				index = index - 1;
			valIndex = valIndex + 1;
			averagePower = averagePower / time
			averages.append(averagePower)




		averagePower = 0
		timeIndex = 0

		for power in averages:
			averagePower = averagePower + power;
			timeIndex += 1

		timeAverage = averagePower / timeIndex;
		max = numpy.amax(averages)

		if max > maxPower:
			maxPower = max

	# print "Max Power for " + str(time) + " seconds"
	# print maxPower

	return maxPower
