import pyrosim.pyrosim as pyrosim


pyrosim.Start_SDF("boxes.sdf")
#pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[x,y,z])
for i in range(6):
    for j in range(6):
        x,y,z = 1,1,1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[i,j,0.5+k] , size=[x,y,z])
            x,y,z = 0.9*x,0.9*y,0.9*z
pyrosim.End()
