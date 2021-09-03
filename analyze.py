import matplotlib.pyplot as plt
import numpy as np

#print(targetAngles)
'''y = np.load('data/backLegSensorValues.npy')
plt.plot(y)

y1 = np.load('data/frontLegSensorValues.npy')
plt.plot(y1)
plt.legend(labels = ["Back Leg","Front Leg"])

plt.show()
'''
y2 = np.load('data/backLegTargetAngles.npy')
x2 =  np.arange(y2.size)
y3 = np.load('data/frontLegTargetAngles.npy')
plt.plot(x2, y2)
plt.plot(x2, y3)
plt.axis('tight')
plt.legend(labels = ["Front Leg motor values", "Back Leg motor values"], loc = 'center')
plt.show()
