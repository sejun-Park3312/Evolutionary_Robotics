from solution import SOLUTION
import pyrosim.pyrosim as pyrosim
import constant as c
import copy
import numpy as np

class Parallel_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()

        print(self.parents)

        self.child = []
        self.fitness_results = np.zeros((c.numberOfGeneration, 2))
        # self.weights = self.parent.weights

    def Evolve(self):
        for j in range(c.populationSize):
            self.parents[j].Evaluate("GUI")
            print(self.parents[j].fitness)
            print(self.parents[j].weights)
            for i in range(c.numberOfGeneration):
                self.Evolve_For_One_Generation(i, j)

            # print(self.fitness_results, j)

    def Evolve_For_One_Generation(self, iterate, populationSize):
        self.Spawn(populationSize)
        self.Mutate()
        self.child.Evaluate("DIRECT")
        # self.Print(iterate, populationSize)
        self.Select(populationSize)

    def Spawn(self, populationSize):
        self.child = copy.deepcopy(self.parents[populationSize]) # deepcopy: copy all date in the object
        # copy of self.parent's weights and its fitness

    def Mutate(self):
        self.child.Mutate()
        self.child.Create_Brain()

    def Select(self, populationSize):

        if self.parents[populationSize].fitness > self.child.fitness:
            self.parents[populationSize] = self.child
            print('changed!')

        np.save('prev_weights.npy', self.parents[populationSize].weights)

    def Print(self, iterate, populationSize):
        self.fitness_results[iterate, 0] = self.parents[populationSize].fitness
        self.fitness_results[iterate, 1] = self.child.fitness
        print(self.fitness_results[iterate])






