import glob
import os
import random
import math

# Generate initial solution
def generate_initial_solution(cities):
    return random.sample(cities, len(cities))

# Calculate total distance of a tour
def calculate_total_distance(solution):
    total_distance = 0
    num_cities = len(solution)
    for i in range(num_cities):
        total_distance += distance(solution[i], solution[(i + 1) % num_cities])
    return total_distance

# Generate a neighbor solution by swapping two cities
def generate_neighbor_solution(solution):
    new_solution = solution.copy()
    idx1, idx2 = random.sample(range(len(new_solution)), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Calculate the cooling rate
def compute_cooling_rate(current_solution, alpha):
   
    return alpha

# Simulated Annealing TSP algorithm
def simulated_annealing_tsp(cities, Tinit, Tfinal, alpha):
    current_solution = generate_initial_solution(cities)
    current_cost = calculate_total_distance(current_solution)
    T = Tinit

    while T > Tfinal:
        new_solution = generate_neighbor_solution(current_solution)
        new_cost = calculate_total_distance(new_solution)
        delta_C = new_cost - current_cost

        if delta_C < 0 or random.random() < math.exp(-delta_C / T):
            current_solution = new_solution
            current_cost = new_cost

        alpha = compute_cooling_rate(current_solution, alpha)
        T *= alpha

    return current_solution

# Example usage:
# Define your distance function here
def distance(city1, city2):
    # Assume city1 and city2 are tuples containing (x, y) coordinates of the cities
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# path = '.'
# file = os.path.join(path, 'tsp-problem-20-10-3000-2000-1.txt')
# # tsp_file = glob.glob(file)
# with open(file, 'r') as f:
#     no_of_cities = int(f.readline().strip())
#     print(no_of_cities)

# Example usage
with open('tsp-problem-20-10-3000-2000-1.txt', 'r') as f:
    no_of_cities = f.readline().strip()
    # print(no_of_cities)
    cities = []
    for city in no_of_cities:
        cities = [list(map(float ,f.readline().strip().split(" ")))]  
    Tinit = 100
    Tfinal = 0.1
    alpha = 0.9
    print(simulated_annealing_tsp(cities, Tinit, Tfinal, alpha))
