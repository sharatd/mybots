from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
import pybullet as p

class ROBOT:

    def __init__(self):
        self.motors = {}
        #self.physicsClient = p.connect(p.GUI)
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
