import pyrosim.pyrosim as pyrosim

def create_robot():
    pyrosim.Start_URDF('body.urdf')

    pyrosim.Send_Cube(name='body', pos=[0,0,1.5], size=[1,1,1])

    pyrosim.Send_Joint(name='body_Rleg', parent='body', child='Rleg', type='revolute', position=[0.5, 0, 1])
    pyrosim.Send_Cube(name='Rleg', pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.Send_Joint(name='body_Lleg', parent='body', child='Lleg', type='revolute', position=[-0.5,0,1])
    pyrosim.Send_Cube(name='Lleg', pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()