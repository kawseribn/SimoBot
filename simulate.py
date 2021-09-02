import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
planeId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)

#print(backLegSensorValues)
#exit()
for i in range(100):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)
p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)
np.save('data/backLegSensorValues.npy',backLegSensorValues)
np.save('data/frontLegSensorValues.npy',frontLegSensorValues)