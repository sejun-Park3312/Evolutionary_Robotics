import pybullet as p
pysicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
import time
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()