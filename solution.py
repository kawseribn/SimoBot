import numpy
import os
from os import link
import pyrosim.pyrosim as pyrosim
import random
import time
class SOLUTION:
    def __init__(self, myID):
        self.weights = numpy.random.rand(3,2) * 2 -1 
        self.myID = myID
    
    def Start_Simulation(self,directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("start /B python simulate.py "+str(directOrGUI)+" "+str(self.myID))
        #print(file,'==='*50)

    def Wait_For_Simulation_To_End(self):
        
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system('del '+fitnessFileName)
        #print(self.fitness)
        

    
    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn =  random.randint(0,1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id



    def Create_World(self):
        x,y,z = 1,1,1
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[x,y,z])
        pyrosim.End()

    def Create_Body(self):
        x,y,z = 1,1,1
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0.0,1.5] , size=[x,y,z])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
            type = "revolute", position = "1.0 0.0 1.0")
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[x,y,z])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
            type = "revolute", position = "2.0 0.0 1.0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[x,y,z])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        
        for currentRow in range(0,3):
            for currentColumn in range(0,2):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
        

        while not os.path.exists("brain" + str(self.myID) + ".nndf"):
                time.sleep(0.01)