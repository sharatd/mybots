import pybullet as p
import pybullet_data 
import time 
import pyrosim.pyrosim as pyrosim
import numpy
import random
import matplotlib.pylab as plt


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")



pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles = numpy.linspace(numpy.pi, -numpy.pi, 1000)
numpy.save('data\Targetangles.npy', targetAngles)
exit()


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = 'Torso_BackLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-0.15, 0.15),
        maxForce = 500
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId, 
        jointName = 'Torso_FrontLeg',
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-0.15, 0.15),
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
