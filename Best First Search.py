import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, cost):
        if node1 not in self.edges:
            self.edges[node1] = []
        self.edges[node1].append((cost, node2))

def best_first_search(graph, start, goal, heuristic):
    # Priority queue for nodes to explore, starting with the start node
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))
    
    # Track visited nodes to avoid re-exploration
    visited = set()
    
    while open_list:
        # Choose the node with the lowest heuristic score
        _, current = heapq.heappop(open_list)
        
        # Check if we reached the goal
        if current == goal:
            print(f"Goal {goal} reached!")
            return True
        
        # Mark the node as visited
        visited.add(current)
        
        # Explore neighbors
        for cost, neighbor in graph.edges.get(current, []):
            if neighbor not in visited:
                # Add neighbor to the open list with its heuristic score
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                print(f"Exploring {neighbor} from {current}")
    
    print("Goal not reachable")
    return False

# Example graph setup
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 2)
graph.add_edge('D', 'E', 1)

# Define heuristic (estimated cost to reach goal 'E')
heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0
}

# Execute Best-First Search
best_first_search(graph, start='A', goal='E', heuristic=heuristic)
