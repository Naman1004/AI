from collections import deque

# Function to check if a state is valid
def is_valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if 3 - m > 0 and 3 - m < 3 - c:
        return False
    return True

# Function to generate all possible next states
def get_successors(state):
    successors = []
    m, c, b = state
    if b == 1:
        new_states = [
            (m - 1, c, 0), (m - 2, c, 0), (m, c - 1, 0), (m, c - 2, 0), (m - 1, c - 1, 0)
        ]
    else:
        new_states = [
            (m + 1, c, 1), (m + 2, c, 1), (m, c + 1, 1), (m, c + 2, 1), (m + 1, c + 1, 1)
        ]
    
    for new_state in new_states:
        if is_valid(new_state):
            successors.append(new_state)
    return successors

# Function to perform BFS to solve the problem
def missionaries_and_cannibals():
    initial_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [goal_state]
        
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    
    return None

# Solve the problem
solution = missionaries_and_cannibals()

# Print the solution steps
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
