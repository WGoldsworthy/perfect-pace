# Perfect Pace calculator
import helpers
import json
import datetime
import argparse

parser = argparse.ArgumentParser(description='Find the best time and power output for a given climb');
parser.add_argument('-c', metavar='c', help='The name of the climb profile you want to run against')

args = parser.parse_args()

if (args.c):
	profileFile = args.c + '.json'
else:
	profileFile = "testClimb.json"

surface = "asphalt"
position = "aerobars"
height = 0
wind = 0

with open('./data/results/powerCurve.json', 'r') as powerFile:
	powerData = json.load(powerFile)

with open('./data/profiles/' + profileFile, 'r') as file:
	profile = json.load(file);

def roundTo(x, base=30):
    return base * round(x/base)

def getSpeed(power):
	return helpers.speed(power, profile['gradient'], surface, position, height, wind);


def timeTakenForClimb(speed, distance):
	timeInHours = distance / speed
	timeInSeconds = timeInHours * 60 * 60;
	return timeInSeconds


def findBestTimeForClimb():
	power = 700;
	time = timeTakenForClimb(getSpeed(power), profile['distance']);

	isAcheivable = False;

	while (not isAcheivable):
		if (power > powerData[str(roundTo(time, 30))] ):
			power = power - 1
			time = timeTakenForClimb(getSpeed(power), profile['distance']);
		else:
			isAcheivable = True

	print("Perfect pace requires a power of " + str(power));
	print("And be a time of " + str(datetime.timedelta(seconds=time)))


findBestTimeForClimb()