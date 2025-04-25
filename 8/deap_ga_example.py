import random
from deap import base, creator, tools, algorithms # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Define problem: maximize f(x) = x * sin(10πx) + 1 in [0, 1]
def fitness_func(individual):
    x = individual[0]
    return x * np.sin(10 * np.pi * x) + 1,  # comma makes it a tuple

# Create custom fitness + individual
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox setup
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fitness_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run the genetic algorithm
def run_deap():
    pop = toolbox.population(n=20)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=20, 
                                    stats=stats, halloffame=hof, verbose=True)

    print(f"\n🏆 Best solution: x = {hof[0][0]:.4f}, fitness = {hof[0].fitness.values[0]:.4f}")
    
    # Optional: Plot fitness over generations
    gen = log.select("gen")
    fit_max = log.select("max")
    plt.plot(gen, fit_max, label="Max Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Evolution of Fitness using DEAP")
    plt.legend()
    plt.grid()
    plt.show()

run_deap()

