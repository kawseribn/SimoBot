import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)


planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

#targetAngles = numpy.sin(numpy.linspace(-(numpy.pi), +(numpy.pi), 1000))
backLegAmplitude = numpy.pi/4
backLegFrequency = 10
backLegPhaseOffset = numpy.pi/2.2

frontLegAmplitude = numpy.pi/5
frontLegFrequency = 10
frontLegPhaseOffset = numpy.pi/2.6

backLegTargetAngles = backLegAmplitude * numpy.sin(numpy.linspace(-(backLegFrequency * numpy.pi) + backLegPhaseOffset,(backLegFrequency * numpy.pi) + backLegPhaseOffset, num=1000))
frontLegTargetAngles = frontLegAmplitude * numpy.sin(numpy.linspace(-(frontLegFrequency * numpy.pi) + frontLegPhaseOffset,(frontLegFrequency * numpy.pi) + frontLegPhaseOffset, num=1000))



'''numpy.save('data/backLegTargetAngles.npy',backLegTargetAngles)
numpy.save('data/frontLegTargetAngles.npy',frontLegTargetAngles)

exit()'''
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pos = random.uniform(-numpy.pi/2.0,+numpy.pi/2.0)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = 'Torso_Leg1',
    controlMode = p.POSITION_CONTROL,
    targetPosition = backLegTargetAngles[i],
    maxForce = 25)
    time.sleep(1/240)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = 'Torso_Leg2',
    controlMode = p.POSITION_CONTROL,
    targetPosition = frontLegTargetAngles[i],
    maxForce = 30)
    time.sleep(1/240)

p.disconnect()
#print(backLegSensorValues)
#print(frontLegSensorValues)
numpy.save('data/backLegSensorValues.npy',backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy',frontLegSensorValues)
numpy.save('data/backLegTargetAngles.npy',backLegTargetAngles)
numpy.save('data/frontLegTargetAngles.npy',frontLegTargetAngles)