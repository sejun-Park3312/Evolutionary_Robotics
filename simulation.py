import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import os

pysicsClient = p.connect(p.GUI)
p.setRealTimeSimulation(1)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(gravX = 0, gravY = 0, gravZ = -9.8)

planeId = p.loadURDF('plane.urdf')
robotID = p.loadURDF('body.urdf')
pyrosim.Prepare_To_Simulate(robotID)

backLegSV = numpy.zeros(10000)

for i in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link('LLeg')
    backLegSV[i] = backLegTouch
    print(f'step{i}, BackLeg Touch Sonsor Value : {backLegTouch}')
    time.sleep(1/60)
    print(i)
p.disconnect()

data_directory = 'Data'
os.makedirs(data_directory, exist_ok = True)
output_filenames = os.path.join(data_directory, 'backLegSensorValues.npy')
numpy.save(output_filenames, backLegSV)
print(f'sensor values saved to {output_filenames}')