# Perfect Pace calculator
import helpers
import json
import datetime

power = 200
gradient = 0
surface = "asphalt"
position = "aerobars"
height = 0
wind = 0

with open('./data/profiles/testClimb.json', 'r') as file:
	profile = json.load(file);

print(profile)


def getSpeed():
	return helpers.speed(power, profile['gradient'], surface, position, height, wind);


def timeTakenForClimb(speed, distance):
	timeInHours = distance / speed
	timeInSeconds = timeInHours * 60 * 60;
	return str(datetime.timedelta(seconds=timeInSeconds))


# Speed * Time = distance
# Time = distance / speed

print(timeTakenForClimb(getSpeed(), profile['distance']));