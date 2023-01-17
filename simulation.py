from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data 
import pyrosim.pyrosim as pyrosim

class SIMULATION:

    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

