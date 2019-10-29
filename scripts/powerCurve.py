# Get power curve for given time periods

import io
import os
import json
import numpy
import argparse
import sys
import dynamicTimePower

# We want to get the max power at each 30 second interval up to one minute.
# The result should be an array of power and time pairs

powerCurve = {};

timeDiff = 30; # 30 Second gaps
timeStart = 60; # 1 Minute
timeEnd = 3600; # 1 Hour

time = timeStart;

while time < timeEnd:
	maxPower = dynamicTimePower.getMaxPower(time);
	powerCurve[time] = maxPower;
	print "Time: " + str(time) + " Power: " + str(maxPower)
	time = time + timeDiff;

with open('./data/results/powerCurve.json', 'w+') as powerCurveFile:
	json.dump(powerCurve, powerCurveFile, sort_keys=True);

print "Power curve data written to: /data/results.powerCurve.json";
