import pyrosim.pyrosim as pyrosim
import pybullet as p

from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

from sensor import SENSOR
from motor import MOTOR
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system('del brain'+str(self.solutionID)+'.nndf')

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
            #if int(jointName[-1])%2==0:
            if 'BackLeg' in jointName:
                #print(self.motors[jointName].frequency)
                self.motors[jointName].frequency = c.LegFrequency/2
    def ACT(self,t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                jointName = self.nn.Get_Joint_Name(neuronName)
                self.motors[jointName].Set_Value(desiredAngle,self.robot)
               
                

    def Think(self):
        self.nn.Update()
        #self.nn.Print()
    
    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        # print(stateOfLinkZero)
        # print(positionOfLinkZero)
        # print(xCoordinateOfLinkZero)
        f = open("tmp"+str(solutionID)+".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        temp = "tmp"+str(solutionID)+".txt" 
        file =  "fitness"+str(solutionID)+".txt"
        os.system('rename '+temp+' '+file)

