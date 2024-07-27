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
    print("library sudah terimpor")
except ImportError:
    print("Libary belum terimpor")


start = time.time()

df_location = pd.read_excel("tes1 - Copy.xlsx", index_col=0)
distance_df = pd.DataFrame(df_location)

shops_index = distance_df.index
cities = []
for shop in shops_index:
    if(shop == '15000000000000000000000000'):
        continue
    else:
        cities.append(shop)

# get shop's label info
# def getCity():
#     shops_index = distance_df.index
#     cities = []
#     for shop in shops_index:
#         cities.append(shop)
#     return cities

# calculating distance of the cities
def calcDistance(cities):
    fit = 0
    for j in range(len(cities)-1):
      if j == 0:
        loc_source = '15000000000000000000000000'
        loc_1 = cities[j]
        loc_2 = cities[j+1]
        fit += distance_df[loc_source][loc_1]
        fit += distance_df[loc_1][loc_2]
      else:
        loc_1 = cities[j]
        loc_2 = cities[j+1]
        fit += distance_df[loc_1][loc_2]
    return fit

# selecting the population
def selectPopulation(cities, size):
    population = []

    for i in range(size):
        c = cities.copy()
        random.shuffle(c)
        distance = calcDistance(c)
        population.append([distance, c])
    # print(population)
    fitest = sorted(population)[0]

    return population, fitest


# the genetic algorithm
def geneticAlgorithm(
    population,
    lenCities,
    TOURNAMENT_SELECTION_SIZE,
    MUTATION_RATE,
    CROSSOVER_RATE,
    # TARGET,
):
    max_gen = 200
    gen_number = 0
    for i in range(max_gen):
        new_population = []

        # selecting two of the best options we have (elitism)
        new_population.append(sorted(population)[0])
        new_population.append(sorted(population)[1])

        for k in range(int((len(population) - 2) / 2)):
            # CROSSOVER
            random_number = random.random()
            if random_number < CROSSOVER_RATE:
                parent_chromosome1 = sorted(
                    random.choices(population, k=TOURNAMENT_SELECTION_SIZE)
                )[0]
                parent_chromosome2 = sorted(
                    random.choices(population, k=TOURNAMENT_SELECTION_SIZE)
                )[0]
                point = random.randint(0, lenCities - 1)

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
                child_chromosome1 = random.choices(population)[0][1]
                child_chromosome2 = random.choices(population)[0][1]

            # MUTATION
            if random.random() < MUTATION_RATE:
                point1 = random.randint(0, lenCities - 1)
                point2 = random.randint(0, lenCities - 1)
                mutated_child_chromosome1 = child_chromosome1
                mutated_child_chromosome1[point1], mutated_child_chromosome1[point2] = (
                    mutated_child_chromosome1[point2],
                    mutated_child_chromosome1[point1],
                )

                point1 = random.randint(0, lenCities - 1)
                point2 = random.randint(0, lenCities - 1)
                mutated_child_chromosome2 = child_chromosome2
                mutated_child_chromosome2[point1], mutated_child_chromosome2[point2] = (
                    mutated_child_chromosome2[point2],
                    mutated_child_chromosome2[point1],
                )
                if(calcDistance(child_chromosome1) > calcDistance(mutated_child_chromosome1)):
                    child_chromosome1 = mutated_child_chromosome1
                
                if(calcDistance(child_chromosome2) > calcDistance(mutated_child_chromosome2)):
                    child_chromosome2 = mutated_child_chromosome2

            new_population.append([calcDistance(child_chromosome1), child_chromosome1])
            new_population.append([calcDistance(child_chromosome2), child_chromosome2])
        population = new_population
        gen_number += 1

        if gen_number % 10 == 0:
            print(gen_number, sorted(population)[0][0])
        # if sorted(population)[0][0] < TARGET:
        #     break
    answer = sorted(population)[0]
    return answer, gen_number

def main():
    count=1
    while count <=1:
        # initial values
        POPULATION_SIZE =100
        TOURNAMENT_SELECTION_SIZE = 10
        MUTATION_RATE = 0.8
        CROSSOVER_RATE = 0.8
        # TARGET = 450.0

        firstPopulation, firstFitest = selectPopulation(cities, POPULATION_SIZE)
        # tessspopulation = copy.deepcopy(firstPopulation)
        answer, genNumber = geneticAlgorithm(
            firstPopulation,
            len(cities),
            TOURNAMENT_SELECTION_SIZE,
            MUTATION_RATE,
            CROSSOVER_RATE,
            # TARGET,
        )

        print("\n----------------------------------------------------------------")
        print('Count:' + str(count))
        print("Generation: " + str(genNumber))
        print("Population : " + str(POPULATION_SIZE))
        print("Fittest chromosome distance before training: " + str(firstFitest[0]))
        print("Fittest chromosome distance after training: " + str(answer[0]))
        # print("The location: " + str(answer[1]))
        # print("Target distance: " + str(TARGET))
        print("----------------------------------------------------------------\n")
        
        end = time.time()
        execution_time = end-start
        print(execution_time)
        # read= True
        # if(read == True):
        #     with open('AnalisisGA - MR08.json', 'r') as file:
        #         data_GA = json.load(file)
        # else:
        #     data_GA = {}
        # key = f"P-{POPULATION_SIZE}, G-{genNumber}, M-{MUTATION_RATE}, C-{CROSSOVER_RATE}, T-{TOURNAMENT_SELECTION_SIZE} - Count-{count}"
        # if(key not in data_GA):
        #     data_GA[key] = {'Test ke-':count,
        #                     'Population': POPULATION_SIZE,
        #                     'Generation': genNumber,
        #                     'Mutation Rate': MUTATION_RATE,
        #                     'Crossover Rate': CROSSOVER_RATE,
        #                     'Tournamnet Size': TOURNAMENT_SELECTION_SIZE,
        #                     'Distance': answer[0],
        #                     'Execution Time': execution_time,
        #                     'Locations': answer[1]}
        
        
        # # Nama file untuk menyimpan data JSON
        # nama_file = "AnalisisGA - MR08.json"
        # # Menyimpan data ke dalam file JSON
        # with open(nama_file, 'w') as file:
        #     json.dump(data_GA, file)

        # print("Data telah disimpan ke dalam file", nama_file)
        count += 1
    # drawMap(cities, answer)
    # return tessspopulation, firstFitest

# tessspopulation, firstFitest = main()

main()