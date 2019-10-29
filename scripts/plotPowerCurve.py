import matplotlib.pyplot as plt
import json
import numpy as np;
import io
import sys

powerData = [];
times = [];

with open('./data/results/powerCurve.json') as powerCurveFile:
	powerJson = json.load(powerCurveFile);
	time = 60;
	timeDiff = 30;
	timeEnd = 3600;
	while time < timeEnd:
		powerData.append(powerJson[str(time)]);
		times.append(time);
		time = time + timeDiff;

plt.plot(times, powerData);
plt.grid()
plt.show();