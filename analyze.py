import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load('data\sensorvals.npy')
frontLegSensorValues = numpy.load('data\Frontlegsensorvals.npy')

print(backLegSensorValues)
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label = 'back leg sensor', linewidth = 4)
matplotlib.pyplot.plot(frontLegSensorValues, label = 'front leg sensor')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
