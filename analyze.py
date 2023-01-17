import matplotlib.pyplot
import numpy

targetAngles = numpy.load('data\Targetangles.npy')
backLegSensorValues = numpy.load('data\sensorvals.npy')
frontLegSensorValues = numpy.load('data\Frontlegsensorvals.npy')
backlegtargetAngles = numpy.load('data\Targetanglesback.npy')
frontlegtargetAngles = numpy.load('data\Targetanglesfront.npy')

print(targetAngles)
print(backLegSensorValues)
print(frontLegSensorValues)


steps = numpy.linspace(0, 999, 1000)
matplotlib.pyplot.plot(steps, targetAngles)
matplotlib.pyplot.xlabel('Steps')
matplotlib.pyplot.ylabel('Value in Radians')
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.show()

matplotlib.pyplot.plot(backLegSensorValues, label = 'back leg sensor', linewidth = 5)
matplotlib.pyplot.plot(frontLegSensorValues, label = 'front leg sensor')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

matplotlib.pyplot.plot(frontlegtargetAngles, label = 'Front leg motor values', linewidth = 5)
matplotlib.pyplot.plot(backlegtargetAngles, label = 'Back leg motor values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
