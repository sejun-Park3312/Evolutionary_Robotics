from simulation import SIMULATION
import generate as g

g.Generate_Brain()

simulation = SIMULATION(200)
simulation.run()