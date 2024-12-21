import numpy as np
import os
import random
import pyrosim.pyrosim as pyrosim

class SOLUTION:

    def __init__(self):
        self.weights = 2 * np.random.rand(3, 2) - 1 # create an m x n matrix with random numbers from -1 to 1
        self.Create_Brain()
        self.fitness = []

    def Evaluate(self, DirectOrGUI):
        os.system(f"python simulate.py {DirectOrGUI}")
        f = open("fitness.txt")
        val = float(f.read())
        self.fitness = val
        f.close()

    def Mutate(self):
        randomRow = random.randint(0, 2) # choose a random value from [0, 2] inclusive
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name='body', pos=[0, 0, 1.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name='body_Rleg', parent='body', child='Rleg', type='revolute', position=[0.5, 0, 1])
        pyrosim.Send_Cube(name='Rleg', pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name='body_Lleg', parent='body', child='Lleg', type='revolute', position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name='Lleg', pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="body")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Rleg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Lleg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="body_Rleg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="body_Lleg")

        # two nested for loops
        for currentRow in [0, 1, 2]:
            for currentColumn in [0, 1]:
                pyrosim.Send_Synapse(sourceNeuronName= currentRow,
                                     targetNeuronName= currentColumn + 3,
                                     weight= self.weights[currentRow][currentColumn])

        pyrosim.End()