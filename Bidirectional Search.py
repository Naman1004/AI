from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bidirectional_search(self, start, goal):
        if start == goal:
            return [start]

        # Initialize the frontiers for both directions
        start_frontier = deque([start])
        goal_frontier = deque([goal])

        # Initialize the visited sets and parent pointers for both directions
        start_visited = {start: None}
        goal_visited = {goal: None}

        while start_frontier and goal_frontier:
            # Expand the start side
            if self.expand_frontier(start_frontier, start_visited, goal_visited):
                return self.build_path(start_visited, goal_visited)

            # Expand the goal side
            if self.expand_frontier(goal_frontier, goal_visited, start_visited):
                return self.build_path(start_visited, goal_visited)

        return None  # No path found

    def expand_frontier(self, frontier, visited, other_visited):
        current = frontier.popleft()

        for neighbor in self.graph.get(current, []):
            if neighbor not in visited:
                frontier.append(neighbor)
                visited[neighbor] = current

            # If the other side has already visited this node, we have found a meeting point
            if neighbor in other_visited:
                return True

        return False

    def build_path(self, start_visited, goal_visited):
        # Find the meeting point
        intersection = None
        for node in start_visited:
            if node in goal_visited:
                intersection = node
                break

        if not intersection:
            return None

        # Reconstruct the path from start to intersection
        path = []
        current = intersection
        while current:
            path.append(current)
            current = start_visited[current]
        path.reverse()

        # Reconstruct the path from intersection to goal
        current = goal_visited[intersection]
        while current:
            path.append(current)
            current = goal_visited[current]

        return path


# Example usage
g = Graph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), 
    ('E', 'F'), ('F', 'G')
]

for u, v in edges:
    g.add_edge(u, v)

start = 'A'
goal = 'G'

path = g.bidirectional_search(start, goal)
if path:
    print(f"Path found: {path}")
else:
    print("No path found.")
