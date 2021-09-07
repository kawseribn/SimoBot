import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    x,y,z = 1,1,1
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[x,y,z])
    pyrosim.End()


def Generate_Body():
    # x,y,z = 1,1,1
    # pyrosim.Start_URDF("body.urdf")
    # pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[x,y,z])
    # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
    #     type = "revolute", position = "1 0.0 1")
    # pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[x,y,z])
    # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
    #     type = "revolute", position = "2 0.0 1")
    # pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[x,y,z])
    
    # pyrosim.End()
    pyrosim.Start_URDF("body.urdf")
    # Robot Torso
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    # Connect BackLeg to Torso with one joint
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="2.0 0.0 1.0")
    # Robot FrontLeg
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    # Connect FrontLeg to Torso with a second joint.
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="1.0 0.0 1.0")
    # The other BackLeg
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    # End
    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    
    for linkName in range(0,3):
        for motor in range(3,5):
                pyrosim.Send_Synapse( sourceNeuronName = linkName , targetNeuronName = motor , weight =  random.randrange(-1, 1))

    pyrosim.End()





