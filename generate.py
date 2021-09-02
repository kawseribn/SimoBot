import pyrosim.pyrosim as pyrosim


def Create_World():
    x,y,z = 1,1,1
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[2,2,0.5] , size=[x,y,z])
    pyrosim.End()

def Create_Robot():
    x,y,z = 1,1,1
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[x,y,z])
    pyrosim.Send_Joint( name = "Torso_Leg1" , parent= "Torso" , child = "BackLeg" , 
        type = "revolute", position = "1 0.0 1")
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[x,y,z])
    pyrosim.Send_Joint( name = "Torso_Leg2" , parent= "Torso" , child = "FrontLeg" , 
        type = "revolute", position = "2 0.0 1")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[x,y,z])
    
    pyrosim.End()


Create_World()
Create_Robot()