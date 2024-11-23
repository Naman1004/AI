import heapq

class Node:
    def __init__(self, x, y, g=0, h=0, parent=None):
        self.x = x
        self.y = y
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic cost to the goal
        self.parent = parent

    def f(self):
        return self.g + self.h  # Total cost

    def __lt__(self, other):
        return self.f() < other.f()

def heuristic(a, b):
    """Manhattan distance heuristic"""
    return abs(a.x - b[0]) + abs(a.y - b[1])

def a_star(grid, start, goal):
    """
    A* algorithm implementation.
    grid: 2D grid where 0 represents a free cell and 1 represents an obstacle.
    start: Tuple (x, y) of the starting position.
    goal: Tuple (x, y) of the goal position.
    """
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, Node(start[0], start[1], g=0, h=heuristic(Node(*start), goal)))
    closed_set = set()
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while open_list:
        current_node = heapq.heappop(open_list)

        if (current_node.x, current_node.y) in closed_set:
            continue

        # Check if the goal is reached
        if (current_node.x, current_node.y) == goal:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_set.add((current_node.x, current_node.y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = current_node.x + dx, current_node.y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:  # Valid cell
                if (nx, ny) not in closed_set:
                    neighbor = Node(nx, ny, g=current_node.g + 1, h=heuristic(Node(nx, ny), goal), parent=current_node)
                    heapq.heappush(open_list, neighbor)

    return None  # Return None if no path is found

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)  # Starting position
goal = (4, 4)  # Goal position

path = a_star(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")
