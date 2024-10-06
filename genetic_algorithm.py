import random

# Step 1: Parameters
POPULATION_SIZE = 6
MUTATION_RATE = 0.01
GENERATIONS = 20
GENOME_LENGTH = 5

# Step 2: Fitness Function x^2
def fitness_function(individual):
    x = binary_to_int(individual)
    return x ** 2
  
# Step 3: Helper Functions
def generate_individual():
    return [random.randint(0, 1) for _ in range(GENOME_LENGTH)]

def binary_to_int(binary_list):
    return int(''.join(map(str, binary_list)), 2)

def create_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

# select and individual from the population using roulette wheel selection
def select_parent(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i in range(len(population)):
        current += fitnesses[i]
        if current > pick:
            return population[i]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENOME_LENGTH - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# step 4: main genetic algorithm
def genetic_algorithm():
    population = create_population()
    for _ in range(GENERATIONS):
        fitnesses = [fitness_function(individual) for individual in population]
        new_population = []
        best_individual = max(population, key=lambda x: fitness_function(x))
        print(f"Generation {_ + 1}: Best Individual = {best_individual}, Fitness = {fitness_function(best_individual)}")

        # step 5: selection and reproduction
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])

        population = new_population

    best_individual = max(population, key=lambda x: fitness_function(x))
    print(f"Final Best Individual: {best_individual}, Fitness: {fitness_function(best_individual)}")
    return best_individual

# Step 6: Run the genetic algorithm
best_individual = genetic_algorithm()
print(f"Best Individual: {binary_to_int(best_individual)}")




