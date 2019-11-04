# List of functions used to determine speed based on power and weight

import imp
import math

constants = imp.load_source('data.constants', './data/data.py')

gravity = 9.80655;

def gravityComponent(gradient):
	return gravity * math.sin(math.atan( gradient / 100 )) * constants.totalWeight

def rollingResistance(gradient, surface):
	return gravity * math.cos(math.atan( gradient / 100 )) * constants.totalWeight * getRrCoefficient(surface)


def getRrCoefficient(surface):
	coeffecient = {
		"concrete": 0.002,
		"asphalt": 0.005
	}
	return coeffecient.get(surface)

def aeroDrag(position, height, wind, velocity):
	return 0.5 * getDragCoefficient(position) * constants.frontalArea * getAirDensity(height) * velocitySquared(velocity, wind)


def getDragCoefficient(position):
	dragCoefficient = {
		"tops": 0.408,
		"hoods": 0.324,
		"drops": 0.307,
		"aerobars":	0.2914
	}
	return dragCoefficient.get(position)

def velocitySquared(velocity, wind):
	return ((velocity + wind) * 1000 / 3600) * ((velocity + wind) * 1000 / 3600)

def getAirDensity(height):
	# return 1.225 * math.exp(-0.00011856 * height);
	airDensityConstant = 1.22599
	return airDensityConstant

def calculateForces(velocity, gradient, surface, position, height, wind):
	gravForce = gravityComponent(gradient)
	rollingForce = rollingResistance(gradient, surface)
	airResForce = aeroDrag(position, height, wind, velocity)
	forces = {}
	forces['gravForce'] = gravForce
	forces['rollingForce'] = rollingForce
	forces['airResForce'] = airResForce
	return forces

def calculatePower(velocity, gradient, surface, position, height, wind):

	forces = calculateForces(velocity, gradient, surface, position, height, wind)
	totalForce = forces['airResForce'] + forces['gravForce'] + forces['airResForce']
	wheelPower = totalForce * velocity * 1000 / 3600

	return wheelPower;

def speed(power, gradient, surface, position, height, wind):

	epsilon = 0.00001

	lowerVel = -1000
	upperVel = 1000
	midVel = 0
	midPower = calculatePower(midVel, gradient, surface, position, height, wind)

	itCount = 0

	while (itCount < 100):
		if ( abs(midPower - power) < epsilon):
			break

		if (midPower > power):
			upperVel = midVel
		else: 
			lowerVel = midVel

		midVel = (upperVel + lowerVel) / 2;

		midPower = calculatePower(midVel, gradient, surface, position, height, wind)

		itCount = itCount + 1

	return midVel

def printSpeeds(speed):
	print("Speed: " + str(kmphToMph(speed)) + " (mph)")
	print("Speed: " + str(speed) + " (kmph)");

def kmphToMph(speed):
	return speed * 0.621371;

def findSpeedWithParams(power, gradient, surface, position, height, wind):
	print("With parameters where: ")
	print("Gradient: " + str(gradient));
	print("Surface: " + surface);
	print("Riding Position: " + position);
	print("Height above sea level: " +str(height))
	print("Wind speed:" + str(wind))
	print("If you rode at " + str(power) + " watts of power: ")
	printSpeeds(speed(power, gradient, surface, position, height, wind))


# printSpeeds( speed(200, 5, "asphalt", "tops", 300, 0) )

# findSpeedWithParams(250, 0, "asphalt", "aerobars", 0, 0);

