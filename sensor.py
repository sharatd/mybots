import numpy
import constants as c
import pyrosim 


class SENSOR:

    def __init__(self, linkName):
        self.sensors = {}
        self.values = numpy.zeros(c.vectorSize)
        print(self.values)
        
        #self.linkName = SENSOR(self.linkName)
        #self.values = numpy.zeros(c.vectorSize)
        #print(self.values)
