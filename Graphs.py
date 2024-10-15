from collections import defaultdict, deque

# Graph class using an adjacency list
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Depth First Search (DFS) Traversal
    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=' ')
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Breadth First Search (BFS) Traversal
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Create a graph
g = Graph()

# Add edges (Directed graph)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

# Print the graph
print("Graph structure:")
for node in g.graph:
    print(f"{node} -> {g.graph[node]}")

# Perform DFS traversal
print("\nDFS Traversal starting from 'A':")
g.dfs('A')

# Perform BFS traversal
print("\n\nBFS Traversal starting from 'A':")
g.bfs('A')
