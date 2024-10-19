from collections import deque

def bfs(graph, start):
    # Create a queue for BFS and a list to track visited nodes
    queue = deque([start])
    visited = set([start])

    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        print(vertex, end=" ")  # Process the vertex (you can modify this line if needed)

        # Go through all the adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # If a neighbor has not been visited, mark it visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list (undirected graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call BFS function
bfs(graph, 'A')
