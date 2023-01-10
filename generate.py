import pyrosim.pyrosim as pyrosim

length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5
x2, y2, z2 = 1, 0, 1.5

#pyrosim.Start_SDF("world.sdf")
#pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
#for k in range(5):
#    for j in range(5):
#        for i in range(8):
#            pyrosim.Send_Cube(name="Box"+str(i), pos=[x+j, y+k, z+i], size=[length*0.9**i, width*0.9**i, height*0.9**i])
#pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[x2, y2, z2], size=[length, width, height])
#pyrosim.End()

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()