from collections import deque

def water_jug(capacity, target):
    # capacity = (jug1_capacity, jug2_capacity)
    jug1_capacity, jug2_capacity = capacity
    visited = set()
    
    # State is represented as (jug1_current, jug2_current)
    initial_state = (0, 0)
    queue = deque([initial_state])
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        # If we reached the target
        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            return True
        
        # Mark the state as visited
        visited.add((jug1, jug2))
        
        # Possible states
        states = [
            (jug1_capacity, jug2),  # Fill jug 1
            (jug1, jug2_capacity),  # Fill jug 2
            (0, jug2),              # Empty jug 1
            (jug1, 0),              # Empty jug 2
            (min(jug1 + jug2, jug1_capacity), jug2 - (jug1_capacity - jug1) if jug1 + jug2 > jug1_capacity else jug2),  # Pour jug 2 into jug 1
            (jug1 - (jug2_capacity - jug2) if jug1 + jug2 > jug2_capacity else jug1, min(jug1 + jug2, jug2_capacity))  # Pour jug 1 into jug 2
        ]
        
        for state in states:
            if state not in visited:
                queue.append(state)
    
    return False

# Example usage
capacity = (4, 3)  # Jug capacities
target = 2         # Target amount of water
if water_jug(capacity, target):
    print("It is possible to measure the target amount of water.")
else:
    print("It is not possible to measure the target amount of water.")
