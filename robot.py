from pybullet import enableJointForceTorqueSensor

from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import numpy as np
import math as m

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotID = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK('brain.nndf')
        self.desiredAngle1 = []
        self.desiredAngle2 = []
        self.JointSensor = []

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

        for jointName in pyrosim.jointNamesToIndices:
            jointIndex = p.getJointInfo(self.robotID, pyrosim.jointNamesToIndices[jointName])[0]
            p.enableJointForceTorqueSensor(self.robotID, jointIndex)



    def Sense(self, total_time, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(total_time, t)

        for jointName in pyrosim.jointNamesToIndices:
            jointIndex = p.getJointInfo(self.robotID, pyrosim.jointNamesToIndices[jointName])[0]
            jointState = p.getJointState(self.robotID, jointIndex)

        self.JointSensor.append(jointState[0]*180/m.pi)
        os.makedirs('data', exist_ok=True)
        file_path = os.path.join('data', f'JointSV.npy')
        np.save(file_path,self.JointSensor)


    def Prepare_To_Act(self, total_time):
        for jointName in pyrosim.jointNamesToIndices:
            # print(jointName)
            self.motors[jointName] = MOTOR(self, jointName, total_time)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = m.pi/6
                # jointName = jointName.decode("utf-8")
                self.motors[jointName].Set_Value(desiredAngle)
                # print(f"{neuronName}\t{jointName}\t{desiredAngle}\n")

    def Think(self):
        self.nn.Update()
        # self.nn.Print()