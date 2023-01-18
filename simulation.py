from world import WORLD
from robot import ROBOT
from sensor import SENSOR
import time 
import numpy
import pybullet as p
import pybullet_data 
import pyrosim.pyrosim as pyrosim
import constants as c

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()
        exit()
        
        
        self.amplitude_backleg = c.amplitude_backleg
        self.frequency_backleg = c.frequency_backleg
        self.phaseOffset_backleg = c.phaseOffset_backleg

        self.amplitude_frontleg = c.amplitude_frontleg
        self.frequency_frontleg = c.frequency_frontleg
        self.phaseOffset_frontleg = c.phaseOffset_frontleg


        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.planeId = p.loadURDF("plane.urdf")
        #self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")
        #pyrosim.Prepare_To_Simulate(self.robotId)
        

        self.backLegSensorValues = numpy.zeros(c.vectorSize)
        self.frontLegSensorValues = numpy.zeros(c.vectorSize)
        self.backLegMotorValues = numpy.zeros(c.vectorSize)
        self.frontLegMotorValues = numpy.zeros(c.vectorSize)


        self.targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.vectorSize)
        self.targetAngles_backleg = self.amplitude_backleg * numpy.sin(self.frequency_backleg * self.targetAngles + self.phaseOffset_backleg)
        self.targetAngles_frontleg = self.amplitude_frontleg * numpy.sin(self.frequency_frontleg * self.targetAngles + self.phaseOffset_frontleg)

    def Run(self):
        
        for i in range(c.vectorSize):
            
            p.stepSimulation()
            self.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            self.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robotId,
                jointName = 'Torso_BackLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.targetAngles_backleg[i],
                maxForce = c.maxForce
            )
            pyrosim.Set_Motor_For_Joint(
                bodyIndex = self.robot.robotId, 
                jointName = 'Torso_FrontLeg',
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.targetAngles_frontleg[i],
                maxForce = c.maxForce
            )
            time.sleep(1/60)
            print(i)

    def __del__(self):
        p.disconnect()
    

