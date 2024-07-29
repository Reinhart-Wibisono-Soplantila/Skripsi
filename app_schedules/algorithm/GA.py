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

    # calculating distance of the cities
    def calcDistance(self, cities):
        fit = 0
        for j in range(len(cities)-1):
            if j == 0:
                loc_source = '15000000000000000000000000'
                loc_1 = cities[j]
                loc_2 = cities[j+1]
                fit += self.distance_df[loc_source][loc_1]
                fit += self.distance_df[loc_1][loc_2]
            else:
                loc_1 = cities[j]
                loc_2 = cities[j+1]
                fit += self.distance_df[loc_1][loc_2]
        return fit

    # selecting the population
    def selectPopulation(self, cities, size):
        population = []
        for i in range(size):
            c = cities.copy()
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
                    if(self.calcDistance(child_chromosome1) > self.calcDistance(mutated_child_chromosome1)):
                        child_chromosome1 = mutated_child_chromosome1
                    
                    if(self.calcDistance(child_chromosome2) > self.calcDistance(mutated_child_chromosome2)):
                        child_chromosome2 = mutated_child_chromosome2

                new_population.append([self.calcDistance(child_chromosome1), child_chromosome1])
                new_population.append([self.calcDistance(child_chromosome2), child_chromosome2])
            population = new_population
            gen_number += 1

            print(gen_number, sorted(population)[0][0])
            best = sorted(population)[0][0] 
            if targetCounter == 20:
                stop_iteration == True
                print('It was Stoped')
                break
            else:
                if best < TARGET:
                    TARGET = best
                    targetCounter=0
                else:
                    targetCounter+=1
        answer = sorted(population)[0]
        return answer, gen_number

    def main(self, cities):
        count=1
        while count <=1:
            # initial values
            POPULATION_SIZE =100
            TOURNAMENT_SELECTION_SIZE = 10
            MUTATION_RATE = 0.8
            CROSSOVER_RATE = 0.8

            firstPopulation, firstFitest = self.selectPopulation(cities, POPULATION_SIZE)
            
            TARGET = firstFitest[0]# tessspopulation = copy.deepcopy(firstPopulation)
            answer, genNumber = self.geneticAlgorithm(
                firstPopulation,
                len(cities),
                TOURNAMENT_SELECTION_SIZE,
                MUTATION_RATE,
                CROSSOVER_RATE,
                TARGET,
            )

            print("\n----------------------------------------------------------------")
            print('Count:' + str(count))
            print("Generation: " + str(genNumber))
            print("Population : " + str(POPULATION_SIZE))
            print("Fittest chromosome distance before training: " + str(firstFitest[0]))
            print("Fittest chromosome distance after training: " + str(answer[0]))
            print("The location: " + str(answer[1]))
            # print("Target distance: " + str(TARGET))
            print("----------------------------------------------------------------\n")
            
            end = self.time.time()
            execution_time = end-self.start
            print( 'Time: ',execution_time)
            return  answer, genNumber 
            count +=1
