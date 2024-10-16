# DFS implementation in Python

# Using a graph represented as an adjacency list
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    print(start, end=' ')  # You can store this result instead of printing

    # Visit all the neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal: ")
dfs(graph, 'A')
