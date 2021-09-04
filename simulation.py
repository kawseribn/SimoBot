import pybullet as p
import pybullet_data
import constants as c
import time 
import numpy
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()
        
        
    def Run(self):
        
        #targetAngles = numpy.sin(numpy.linspace(-(numpy.pi), +(numpy.pi), 1000))

        #backLegTargetAngles = c.backLegAmplitude * numpy.sin(numpy.linspace(-(c.backLegFrequency * numpy.pi) + c.backLegPhaseOffset,(c.backLegFrequency * numpy.pi) + c.backLegPhaseOffset, num=1000))
        #frontLegTargetAngles = c.frontLegAmplitude * numpy.sin(numpy.linspace(-(c.frontLegFrequency * numpy.pi) + c.frontLegPhaseOffset,(c.frontLegFrequency * numpy.pi) + c.frontLegPhaseOffset, num=1000))


        for i in range(c.timeStep):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.ACT(i)
            time.sleep(c.sleep)
    def __del__(self):
        p.disconnect()