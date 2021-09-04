import numpy
import constants as c
import time
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        
    def Prepare_To_Act(self):
        self.amplitude = c.LegAmplitude
        self.frequency = c.LegFrequency
        self.offset = c.LegPhaseOffset

        self.motorValues = self.amplitude * numpy.sin(numpy.linspace(-(self.frequency * numpy.pi) + self.offset,(self.frequency * numpy.pi) + self.offset, num=1000))
       #self.frontLegTargetAngles = self.frontLegAmplitude * numpy.sin(numpy.linspace(-(self.frontLegFrequency * numpy.pi) + self.frontLegPhaseOffset,(self.frontLegFrequency * numpy.pi) + self.frontLegPhaseOffset, num=1000))
        
    def Set_Value(self,t,robot):

        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition =  self.motorValues[t],
            maxForce = c.maxForceTorso_Leg1)
