import pybullet as p
import pybullet_data 
import time 
import pyrosim.pyrosim as pyrosim
import numpy
import random
import matplotlib.pylab as plt

amplitude_backleg = numpy.pi/4
frequency_backleg = 5
phaseOffset_backleg = numpy.pi/4

amplitude_frontleg = numpy.pi/4
frequency_frontleg = 5
phaseOffset_frontleg = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")



pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
backLegMotorValues = numpy.zeros(1000)
frontLegMotorValues = numpy.zeros(1000)

targetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
targetAngles_backleg = amplitude_backleg * numpy.sin(frequency_backleg * targetAngles + phaseOffset_backleg)
targetAngles_frontleg = amplitude_frontleg * numpy.sin(frequency_frontleg * targetAngles + phaseOffset_frontleg)
#numpy.save('data\Targetanglesback.npy', targetAngles_backleg)
#numpy.save('data\Targetanglesfront.npy', targetAngles_frontleg)
#exit()


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_backleg[i],
        maxForce = 500
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId, 
        jointName = 'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_frontleg[i],
        maxForce = 500
    )
    #print(backLegTouch)
    time.sleep(1/60)
    #print(i)
numpy.save('data\sensorvals.npy', backLegSensorValues)
numpy.save('data\Frontlegsensorvals.npy', frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)
