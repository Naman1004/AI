import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue to store (cost, node, path)
    priority_queue = [(0, start, [])]
    visited = set()
    
    while priority_queue:
        (cost, current_node, path) = heapq.heappop(priority_queue)
        
        # Add current node to the visited set
        if current_node in visited:
            continue
        
        # Add the current node to the path
        path = path + [current_node]
        
        # If the goal is reached, return the cost and the path
        if current_node == goal:
            return (cost, path)
        
        # Mark node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))
    
    return float("inf"), []  # Return infinity if no path is found

# Example graph: adjacency list (node, cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start = 'A'
goal = 'D'

# Call the uniform cost search function
cost, path = uniform_cost_search(graph, start, goal)

print(f"Least cost: {cost}")
print(f"Path: {' -> '.join(path)}")
