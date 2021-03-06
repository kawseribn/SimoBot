import numpy
import os
from os import link
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 -1 
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
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn =  random.randint(0,c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id



    def Create_World(self):
        x,y,z = 1,1,1
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[x,y,z])
        pyrosim.End()

    def Create_Body(self):
        x,y,z = 1,1,1
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[x,y,z])

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
            type = "revolute", position = "0.0 -0.5 1.0", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0] , size=[0.2, 1, 0.2])

        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
            type = "revolute", position = "0.0 0.5 1.0", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

        #l=left, r = right, b =back, f - front, ll = left lower, rl = right lower, bl = back lower 

        #left
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position="-0.5 0.0 1.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        #right
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position="0.5 0.0 1.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        # ll
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position="-1.0 0.0 0.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # rl
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position="1.0 0.0 0.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
       
        

        # bl
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position="0.0 -1.0 0.0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # fl
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position="0.0 1.0 0.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{}.nndf".format(self.myID))
        #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        

        # pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=0, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLowerLeg")
       

        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="RightLeg_RightLowerLeg")
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                    pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()