from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy

class ROBOT:

    def __init__(self):
        self.motors = {}
        #self.physicsClient = p.connect(p.GUI)
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)
            self.sensors[sensor].Save_Values(i)
        #self.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    
    def Prepare_To_Act(self):
        # self.amplitude = numpy.pi/4
        # self.frequency = 5
        # self.offset = 0
        # self.targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.vectorSize)
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, i):
        for motor in self.motors:
            self.motors[motor].Set_Value(i, self.robotId)
            self.motors[motor].Save_Values(i, self.robotId)