import pyrosim.pyrosim as pyrosim

def create_robot():
    pyrosim.Start_URDF('body.urdf')

    pyrosim.Send_Cube(name='Torso', pos=[0,0,0.5] , size=[1,1,1])

    pyrosim.Send_Joint(name = 'Torso_R_Leg', parent = 'Torso', child = 'R_Leg', type = 'fixed', position = [0.5, 0, 1.5])
    pyrosim.Send_Cube(name = 'R_Leg', pos = [0.5,0,0], size = [1,1,1])

    pyrosim.Send_Joint(name = 'Torso_L_Leg', parent = 'Torso', child = 'L_Leg', type = 'fixed', position = [-0.5, 0, 1.5])
    pyrosim.Send_Cube(name = 'L_Leg', pos = [-0.5,0,0], size = [1,1,1])

    pyrosim.End()
