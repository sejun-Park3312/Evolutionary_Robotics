import pybullet as p
pysicsClient = p.connect(p.GUI)

p.stepSimulation()
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.disconnect()


ab = 10

ac = 20