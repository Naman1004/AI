class State:
    def __init__(self, block_position, goal_position):
        self.block_position = block_position
        self.goal_position = goal_position

    def is_goal(self):
        return self.block_position == self.goal_position

    def __repr__(self):
        return f"State(block_position={self.block_position}, goal_position={self.goal_position})"

class MeansEndAnalysis:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.actions = [
            ("move_block", self.move_block),
        ]

    def move_block(self, state):
        """Action to move the block to the goal position."""
        if state.block_position != state.goal_position:
            return State(state.goal_position, state.goal_position)
        return state

    def solve(self):
        current_state = self.initial_state
        print("Initial State:", current_state)

        # Start solving using means-end analysis
        steps = []
        while not current_state.is_goal():
            print(f"Current state: {current_state}")
            action_taken = None

            # Check for possible actions
            for action, func in self.actions:
                new_state = func(current_state)
                if new_state != current_state:
                    action_taken = action
                    current_state = new_state
                    steps.append(action_taken)
                    break
            
            if action_taken is None:
                print("No valid actions found, unable to proceed.")
                return None
        
        print("Goal achieved!")
        return steps


# Example of usage
initial_state = State(block_position=0, goal_position=5)
mea = MeansEndAnalysis(initial_state)

steps = mea.solve()
if steps:
    print("Steps to solve the problem:", steps)
