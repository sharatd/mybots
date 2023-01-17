import pybullet as p
import pybullet_data 
import time 
import pyrosim.pyrosim as pyrosim
import numpy
import random
import matplotlib.pylab as plt
import constants as c

amplitude_backleg = c.amplitude_backleg
frequency_backleg = c.frequency_backleg
phaseOffset_backleg = c.phaseOffset_backleg

amplitude_frontleg = c.amplitude_frontleg
frequency_frontleg = c.frequency_frontleg
phaseOffset_frontleg = c.phaseOffset_frontleg

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")



pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(c.vectorSize)
frontLegSensorValues = numpy.zeros(c.vectorSize)
backLegMotorValues = numpy.zeros(c.vectorSize)
frontLegMotorValues = numpy.zeros(c.vectorSize)

targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.vectorSize)
targetAngles_backleg = amplitude_backleg * numpy.sin(frequency_backleg * targetAngles + phaseOffset_backleg)
targetAngles_frontleg = amplitude_frontleg * numpy.sin(frequency_frontleg * targetAngles + phaseOffset_frontleg)
#numpy.save('data\Targetanglesback.npy', targetAngles_backleg)
#numpy.save('data\Targetanglesfront.npy', targetAngles_frontleg)
#exit()


for i in range(c.vectorSize):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_backleg[i],
        maxForce = c.maxForce
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId, 
        jointName = 'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_frontleg[i],
        maxForce = c.maxForce
    )
    #print(backLegTouch)
    time.sleep(1/60)
    #print(i)
numpy.save('data\sensorvals.npy', backLegSensorValues)
numpy.save('data\Frontlegsensorvals.npy', frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)
