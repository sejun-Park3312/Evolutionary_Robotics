import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import os
import generate as g

g.create_robot()

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.loadURDF('plane.urdf')
p.loadURDF('body.urdf')


for i in range(500):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()