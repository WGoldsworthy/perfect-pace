# Get average power given a ride data file

import io
import json

with open('./data/rideData.json', 'r') as file:
	rideDataDict = json.load(file);

averagePower = 0;
index = 0;

for value in rideDataDict['watts_calc']:
	# print value
	averagePower = averagePower + value;
	index = index + 1;

averagePower = averagePower / index;

print averagePower;

# print rideDataDict['watts_calc'];