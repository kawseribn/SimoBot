import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self,linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.timeStep)
        #print(self.values)
    def Get_Value(self,t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        '''if t==1000-1:
            print(self.values)'''
        return self.values
    def Save_Values(self, vectorName):
        numpy.save('data/{}.npy'.format(vectorName),self.values)