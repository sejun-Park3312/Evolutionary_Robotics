import pybullet as p
physicsClient = p.connect(p.GUI)
import time
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()
