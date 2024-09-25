import itertools

# Function to calculate the total distance of a given path
def calculate_total_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    # Add distance to return to the starting point
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

# Function to solve TSP using brute force
def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    
    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(cities)
    
    # Initialize the best path and minimum distance
    best_path = None
    min_distance = float('inf')
    
    # Check each permutation
    for perm in all_permutations:
        current_distance = calculate_total_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm
    
    return best_path, min_distance

# Example usage
if __name__ == "__main__":
    # Example distance matrix (symmetric TSP)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    best_path, min_distance = tsp_brute_force(distance_matrix)
    print("Best path:", best_path)
    print("Minimum distance:", min_distance)
