import pyrosim.pyrosim as pyrosim

def create_robot():
    pyrosim.Start_URDF('body.urdf')

    pyrosim.Send_Cube(name='body', pos=[0,0,1.5], size=[1,1,1])

    pyrosim.Send_Joint(name='body_Rleg', parent='body', child='Rleg', type='revolute', position=[0.5, 0, 1])
    pyrosim.Send_Cube(name='Rleg', pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.Send_Joint(name='body_Lleg', parent='body', child='Lleg', type='revolute', position=[-0.5,0,1])
    pyrosim.Send_Cube(name='Lleg', pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    pyrosim.End()