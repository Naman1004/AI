def graph_coloring(graph):
    # Get the number of vertices
    num_vertices = len(graph)

    # Initialize all vertices with no color (-1)
    result = [-1] * num_vertices

    # Assign the first color to the first vertex
    result[0] = 0

    # A temporary array to keep track of available colors
    available = [False] * num_vertices

    # Assign colors to remaining vertices
    for u in range(1, num_vertices):
        # Process all adjacent vertices and mark their colors as unavailable
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = True

        # Find the first available color
        color = 0
        while color < num_vertices and available[color]:
            color += 1

        # Assign the found color
        result[u] = color

        # Reset the values back to False for the next iteration
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = False

    # Print the result
    for vertex in range(num_vertices):
        print(f"Vertex {vertex} ---> Color {result[vertex]}")

# Example usage
graph = [
    [1, 2],     # Edges for vertex 0
    [0, 2, 3],  # Edges for vertex 1
    [0, 1, 3],  # Edges for vertex 2
    [1, 2]      # Edges for vertex 3
]

graph_coloring(graph)
