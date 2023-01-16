import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('data\sensorvals.npy')
frontLegSensorValues = numpy.load('data\Frontlegsensorvals.npy')

print(backLegSensorValues)
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
