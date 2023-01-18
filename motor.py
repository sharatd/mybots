import numpy

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        MOTOR.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = numpy.pi/4
        self.frequency = 5
        self.offset = 0
        #self.backLegMotorValues = numpy.zeros(c.vectorSize)
        #self.frontLegMotorValues = numpy.zeros(c.vectorSize)