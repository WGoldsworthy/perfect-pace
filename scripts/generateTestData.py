# Generate some test data of pacing strategy and final time

import json
import perfectPace
from random import random

# Either sample at a set distance or every second.
sampleMetric = 10; # 1 metres

with open('./data/profiles/UHC.json') as file:
	climb = json.load(file);

with open('./data/results/powerCurve.json') as powerFile:
	powerData = json.load(powerFile);

def getClimbProfile(climb):
	climbProfile = []
	i = 0;
	while climb['grade_smooth'][i] >= 0:
		climbPoint={}
		climbPoint['distance'] = climb['distance'][i];
		climbPoint['gradient'] = climb['grade_smooth'][i];
		climbProfile.append(climbPoint)
		i = i + 1
		
	return climbProfile


# Result should be a tuple list of distance and power
def generateStrategy(climbProfile):
	startingPower = round(random() * 700);
	print(startingPower)
	speed = perfectPace.getSpeed(startingPower, climbProfile[0]['gradient'])
	print(speed)


# def averagePower(powerPoints):


print(getClimbProfile(climb))


generateStrategy(getClimbProfile(climb))