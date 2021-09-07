import pybullet as p
import pybullet_data
import constants as c
import time 
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self,directOrGUI, solutionID):
        self.directOrGUI  = directOrGUI 
        self.solutionID = solutionID

        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        

        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)
        
        
    def Run(self):
        
        #targetAngles = numpy.sin(numpy.linspace(-(numpy.pi), +(numpy.pi), 1000))

        #backLegTargetAngles = c.backLegAmplitude * numpy.sin(numpy.linspace(-(c.backLegFrequency * numpy.pi) + c.backLegPhaseOffset,(c.backLegFrequency * numpy.pi) + c.backLegPhaseOffset, num=1000))
        #frontLegTargetAngles = c.frontLegAmplitude * numpy.sin(numpy.linspace(-(c.frontLegFrequency * numpy.pi) + c.frontLegPhaseOffset,(c.frontLegFrequency * numpy.pi) + c.frontLegPhaseOffset, num=1000))


        for i in range(c.timeStep):
            if self.directOrGUI == 'GUI':
                time.sleep(c.sleep)
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.ACT(i)
            
            
                     
    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionID)
        

    def __del__(self):
        p.disconnect()