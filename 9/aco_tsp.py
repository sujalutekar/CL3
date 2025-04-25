import numpy as np # type: ignore
import random
import matplotlib.pyplot as plt # type: ignore

# Number of cities
N = 5

# Coordinates of cities
cities = np.random.rand(N, 2)

# Distance matrix
dist_matrix = np.linalg.norm(cities[:, None] - cities, axis=2)

# ACO parameters
NUM_ANTS = 10
NUM_ITER = 50
ALPHA = 1      # Pheromone importance
BETA = 5       # Distance importance
EVAPORATION = 0.5
Q = 100        # Pheromone deposit factor

# Initialize pheromones
pheromones = np.ones((N, N))

# Probability to choose next city
def probability(from_city, unvisited, pheromones, distances):
    pher = np.power(pheromones[from_city][unvisited], ALPHA)
    dist = np.power(1.0 / distances[from_city][unvisited], BETA)
    probs = pher * dist
    return probs / np.sum(probs)

# Build path for one ant
def build_path(pheromones, distances):
    path = []
    visited = set()
    current = random.randint(0, N - 1)
    path.append(current)
    visited.add(current)

    while len(path) < N:
        unvisited = list(set(range(N)) - visited)
        probs = probability(current, unvisited, pheromones, distances)
        next_city = random.choices(unvisited, weights=probs, k=1)[0]
        path.append(next_city)
        visited.add(next_city)
        current = next_city

    return path

# Calculate total path length
def path_length(path, distances):
    return sum(distances[path[i]][path[i + 1]] for i in range(N - 1)) + distances[path[-1]][path[0]]

# ACO main loop
best_path = None
best_length = float('inf')

for iteration in range(NUM_ITER):
    all_paths = []
    all_lengths = []

    for _ in range(NUM_ANTS):
        path = build_path(pheromones, dist_matrix)
        length = path_length(path, dist_matrix)
        all_paths.append(path)
        all_lengths.append(length)

        if length < best_length:
            best_length = length
            best_path = path

    # Update pheromones
    pheromones *= (1 - EVAPORATION)

    for path, length in zip(all_paths, all_lengths):
        for i in range(N):
            from_city = path[i]
            to_city = path[(i + 1) % N]
            pheromones[from_city][to_city] += Q / length
            pheromones[to_city][from_city] += Q / length

    print(f"Iteration {iteration + 1}: Best length = {best_length:.4f}")

# 🏁 Show result
print(f"\n🚀 Shortest path: {best_path} | Length: {best_length:.4f}")

# 🗺️ Plot
x = [cities[i][0] for i in best_path + [best_path[0]]]
y = [cities[i][1] for i in best_path + [best_path[0]]]
plt.plot(x, y, marker='o')
plt.title("Shortest Path using Ant Colony Optimization")
plt.grid(True)
plt.show()
