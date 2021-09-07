from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('del brain*.nndf')
        os.system('del tmp*.txt')
        os.system('del fitness*.txt')
        self.parents = {}
        self.nextAvailableID = 0

        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):

        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Evaluate(self, solutions):
        for pop in range(c.populationSize):
            solutions[pop].Start_Simulation("DIRECT")
        for pop in range(c.populationSize):
            solutions[pop].Wait_For_Simulation_To_End()    

    
    def Spawn(self):
        self.children = {}
        for pop in self.parents:
            self.children[pop] = copy.deepcopy(self.parents[pop])
            self.children[pop].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
       

    def Mutate(self):
        #self.child.Mutate()
        for pop in self.children:
            self.children[pop].Mutate()

    def Select(self):
        for pop in self.parents:
            if self.parents[pop].fitness > self.children[pop].fitness:
                self.parents = self.children

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        for pop in range(len(self.parents.keys()) - 1):
            if self.parents[pop].fitness < self.parents[pop + 1].fitness:
                bestParent = self.parents[pop]
            else:
                bestParent = self.parents[pop + 1]

        bestParent.Start_Simulation("GUI")

    def Print(self):
        for key in self.parents:
            print('\n'*1,'-'*50,'\n'*1, 'Parents Fitness : ',self.parents[key].fitness,"|", 'Childs fitness', self.children[key].fitness,'\n'*1,'-'*50,'\n'*1,)