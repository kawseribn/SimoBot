import matplotlib.pyplot as plt
import numpy


y2 = numpy.load('data/backLegTargetAngles.npy')
x2 =  numpy.arange(y2.size)
y3 = numpy.load('data/frontLegTargetAngles.npy')
plt.plot(x2, y2)
plt.plot(x2, y3)
plt.axis('tight')
plt.legend(labels = ["Front Leg motor values", "Back Leg motor values"], loc = 'center')
plt.show()
