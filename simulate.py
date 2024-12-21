from simulation import SIMULATION
import sys

DirectOrGUI = sys.argv[1]

simulation = SIMULATION(100, DirectOrGUI)
simulation.run()
simulation.Get_Fitness()