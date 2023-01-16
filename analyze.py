import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('data\sensorvals.npy')
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()