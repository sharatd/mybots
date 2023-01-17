import matplotlib.pyplot
import numpy

targetAngles = numpy.load('data\Targetangles.npy')
backLegSensorValues = numpy.load('data\sensorvals.npy')
frontLegSensorValues = numpy.load('data\Frontlegsensorvals.npy')

print(targetAngles)
print(backLegSensorValues)
print(frontLegSensorValues)

targetAngles = numpy.sin(targetAngles)/1.25
steps = numpy.linspace(0, 999, 1000)
matplotlib.pyplot.plot(steps, targetAngles)
matplotlib.pyplot.xlabel('Angle [rad]')
matplotlib.pyplot.ylabel('sin(x)')
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(backLegSensorValues, label = 'back leg sensor', linewidth = 4)
matplotlib.pyplot.plot(frontLegSensorValues, label = 'front leg sensor')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
