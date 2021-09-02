import matplotlib.pyplot as plt
import numpy as np

y = np.load('data/backLegSensorValues.npy')
plt.plot(y)

y1 = np.load('data/frontLegSensorValues.npy')
plt.plot(y1)
plt.legend(labels = ["Back Leg","Front Leg"])

plt.show()