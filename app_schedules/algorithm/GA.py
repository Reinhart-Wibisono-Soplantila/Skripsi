from django.contrib.staticfiles import finders
class GeneticAlgorithm:
    def __init__(self):
        try:    
            import pandas as pd
            import numpy as np
            import math
            import random
            import string
            import copy
            # import matplotlib.pyplot as plt
            import json
            import time
            self.np = np
            self.pd = pd
            self.random = random
            self.copy = copy
            self.time = time

            file_path = finders.find('files/DistanceMatriks.xlsx')
            self.distance_df = pd.read_excel(file_path, engine='openpyxl', index_col=0)
            self.start = time.time()
            print("library sudah terimpor")
        except ImportError:
            print("Libary belum terimpor")

    # calculating distance of the outlets
    def calcDistance1(self, outlets):
        fit = 0
        print("")
        print("***********")
        print("")
        for j in range(len(outlets)-1):
            if j == 0:
                loc_source = '15000000000000000000000000'
                loc_1 = outlets[j]
                loc_2 = outlets[j+1]
                fit += self.distance_df[loc_source][loc_1]
                print('loc_source', loc_source)
                print('loc1', loc_1)
                print('fit' ,fit)
                fit += self.distance_df[loc_1][loc_2]
                print('loc2', loc_2)
                print(fit)
            else:
                loc_1 = outlets[j]
                loc_2 = outlets[j+1]
                fit += self.distance_df[loc_1][loc_2]
                print('loc1', loc_1)
                print('loc2', loc_2)
                print('fit', fit)
                
        return fit
    def calcDistance(self, items):
        fit = 0
        for j in range(len(items)-1):
            if j == 0:
                loc_source = '15000000000000000000000000'
                loc_1 = items[j]
                loc_2 = items[j+1]
                fit += self.distance_df[loc_source][loc_1]
                fit += self.distance_df[loc_1][loc_2]
            else:
                loc_1 = items[j]
                loc_2 = items[j+1]
                fit += self.distance_df[loc_1][loc_2]
        return fit

    # selecting the population
    def selectPopulation(self, outlets, size):
        population = []
        for i in range(size):
            c = outlets.copy()
            self.random.shuffle(c)
            distance = self.calcDistance(c)
            population.append([distance, c])
        # print(population)
        fitest = sorted(population)[0]

        return population, fitest


    # the genetic algorithm
    def geneticAlgorithm(
        self,
        population,
        lenCities,
        TOURNAMENT_SELECTION_SIZE,
        MUTATION_RATE,
        CROSSOVER_RATE,
        TARGET
    ):
        # max_gen = 200
        stop_iteration = False
        targetCounter = 0
        gen_number = 0
        while(stop_iteration == False):
            new_population = []

            # selecting two of the best options we have (elitism)
            new_population.append(sorted(population)[0])
            new_population.append(sorted(population)[1])

            for k in range(int((len(population) - 2) / 2)):
                # CROSSOVER
                random_number = self.random.random()
                if random_number < CROSSOVER_RATE:
                    # print('cross')
                    parent_chromosome1 = sorted(
                        self.random.choices(population, k=TOURNAMENT_SELECTION_SIZE)
                    )[0]
                    parent_chromosome2 = sorted(
                        self.random.choices(population, k=TOURNAMENT_SELECTION_SIZE)
                    )[0]
                    point = self.random.randint(0, lenCities - 1)

                    child_chromosome1 = parent_chromosome1[1][0:point]
                    for j in parent_chromosome2[1]:
                        if (j in child_chromosome1) == False:
                            child_chromosome1.append(j)
                    
                    child_chromosome2 = parent_chromosome2[1][0:point]
                    for j in parent_chromosome1[1]:
                        if (j in child_chromosome2) == False:
                            child_chromosome2.append(j)

                # If crossover not happen
                else:
                    child_chromosome1 = self.random.choices(population)[0][1]
                    child_chromosome2 = self.random.choices(population)[0][1]

                # MUTATION
                if self.random.random() < MUTATION_RATE:
                    # print('mutasi')
                    point1 = self.random.randint(0, lenCities - 1)
                    point2 = self.random.randint(0, lenCities - 1)
                    mutated_child_chromosome1 = child_chromosome1
                    mutated_child_chromosome1[point1], mutated_child_chromosome1[point2] = (
                        mutated_child_chromosome1[point2],
                        mutated_child_chromosome1[point1],
                    )

                    point1 = self.random.randint(0, lenCities - 1)
                    point2 = self.random.randint(0, lenCities - 1)
                    mutated_child_chromosome2 = child_chromosome2
                    mutated_child_chromosome2[point1], mutated_child_chromosome2[point2] = (
                        mutated_child_chromosome2[point2],
                        mutated_child_chromosome2[point1],
                    )
                    distChild1 = self.calcDistance(child_chromosome1)
                    distMutatedChild1 =  self.calcDistance(mutated_child_chromosome1)
                    distChild2 = self.calcDistance(child_chromosome2)
                    distMutatedChild2 =  self.calcDistance(mutated_child_chromosome2)
                    
                    if distChild1>distMutatedChild1:
                        new_population.append([distMutatedChild1, mutated_child_chromosome1])
                    
                    if distChild2 > distMutatedChild2:
                        new_population.append([distMutatedChild2, mutated_child_chromosome2])
                else:
                    new_population.append([self.calcDistance(child_chromosome1), child_chromosome1])
                    new_population.append([self.calcDistance(child_chromosome2), child_chromosome2])

                # print(k)
                # print(len(new_population))
                # print('')
            population = new_population
            gen_number += 1
            
            sortedlist = sorted(population, key=lambda x: x[0])
            best = sortedlist[0]
            
            print('')
            if(targetCounter == 0):
                print('best:', best)
            print('HITUNG:', self.calcDistance(best[1]))
            print('best:', best[0])
            print('best', best[1])
            print('')
            if targetCounter == 10:
                stop_iteration == True
                print('It was Stoped')
                
                print('jarak', self.calcDistance(best[1]))
                print('best: ', best)
                break
            else:
                if best[0] < TARGET:
                    TARGET = best[0]
                    targetCounter=0
                else:
                    targetCounter+=1
        answer = best
        return answer, gen_number

    def main(self, outlets):
        count=1
        while count <=1:
            # initial values
            POPULATION_SIZE =100
            TOURNAMENT_SELECTION_SIZE = 4
            MUTATION_RATE = 0.8
            CROSSOVER_RATE = 0.8

            firstPopulation, firstFitest = self.selectPopulation(outlets, POPULATION_SIZE)
            # print('len:  ',firstPopulation[0][1])
            TARGET = firstFitest[0]# tessspopulation = copy.deepcopy(firstPopulation)
            answer, genNumber = self.geneticAlgorithm(
                firstPopulation,
                len(outlets),
                TOURNAMENT_SELECTION_SIZE,
                MUTATION_RATE,
                CROSSOVER_RATE,
                TARGET,
            )

            print("\n----------------------------------------------------------------")
            # print('Count:' + str(count))
            # print("Generation: " + str(genNumber))
            # print("Population : " + str(POPULATION_SIZE))
            # print("Fittest chromosome distance before training: " + str(firstFitest[0]))
            # print("Fittest chromosome distance after training: " + str(answer[0]))
            # print("The location: " + str(answer[1]))
            # print("Target distance: " + str(TARGET))
            print("----------------------------------------------------------------\n")
            # valll = self.calcDistance1(answer[1])
                
            end = self.time.time()
            execution_time = end-self.start
            print( 'Time: ',execution_time)
            return  answer, genNumber 
            count +=1
