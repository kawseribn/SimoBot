import pyrosim.pyrosim as pyrosim
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import constants as c
class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            #print(self.sensors[linkName],linkName)
            
    def Sense(self,t):
        #self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #print(self.sensors)
        for i in self.sensors.keys():
            self.sensors[i].Get_Value(t)
        

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            if int(jointName[-1])%2==0:
                print(self.motors[jointName].frequency)
                self.motors[jointName].frequency = c.LegFrequency/2
                print(self.motors[jointName].frequency)
            #print(jointName)
    def ACT(self,t):
        for i in self.motors.keys():
            self.motors[i].Set_Value(t,self.robot)
            #print(self.motors[i])