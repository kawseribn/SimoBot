
import numpy


backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

maxForceTorso_Leg1 = 25
#targetAngles = numpy.sin(numpy.linspace(-(numpy.pi), +(numpy.pi), 1000))
LegAmplitude = numpy.pi/4
LegFrequency = 10
LegPhaseOffset = 0


timeStep = 1000
sleep = 1/240
