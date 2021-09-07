
import numpy


backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

maxForceTorso_Leg1 = 50
#targetAngles = numpy.sin(numpy.linspace(-(numpy.pi), +(numpy.pi), 1000))
LegAmplitude = numpy.pi/4
LegFrequency = 10
LegPhaseOffset = 0


timeStep = 500
sleep = 1/500
numberOfGenerations = 15
populationSize = 10


numSensorNeurons = 7
numMotorNeurons = 14

motorJointRange = 0.29