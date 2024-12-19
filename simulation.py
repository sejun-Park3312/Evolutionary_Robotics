import pybullet as p
import pybullet_data

pysicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(gravX = 0, gravY = 0, gravZ = -9.8)
planeId = p.loadURDF('plane.urdf')
p.loadSDF("box.sdf")
import time
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()