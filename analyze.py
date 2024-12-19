import numpy as np
import matplotlib.pyplot as plt

backLegSensorValue = np.load('data/backLegSensorValues.npy')

simulation_steps = 500
backLegSensorValue = backLegSensorValue[:simulation_steps]

plt.plot(backLegSensorValue, 'o', markersize = 1, label = 'Back Leg')
plt.xlim(0, simulation_steps)
plt.ylim(-1.5, 1.5)

plt.xlabel('sim step')
plt.ylabel('Sensor value')

plt.title('hehehehe')

plt.legend()
plt.show()