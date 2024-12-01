import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.grid[0][0] = 'A'  # Agent's initial position
        self.generate_wumpus()
        self.generate_pits()
        self.place_gold()

    def generate_wumpus(self):
        self.wumpus_pos = (random.randint(1, self.size - 1), random.randint(1, self.size - 1))
        self.grid[self.wumpus_pos[0]][self.wumpus_pos[1]] = 'W'

    def generate_pits(self):
        self.pits = []
        num_pits = random.randint(2, self.size - 1)
        for _ in range(num_pits):
            pit_pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pit_pos not in [self.wumpus_pos, (0, 0)]:
                self.pits.append(pit_pos)
                self.grid[pit_pos[0]][pit_pos[1]] = 'P'

    def place_gold(self):
        self.gold_pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        while self.gold_pos in self.pits or self.gold_pos == self.wumpus_pos or self.gold_pos == (0, 0):
            self.gold_pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        self.grid[self.gold_pos[0]][self.gold_pos[1]] = 'G'

    def display_world(self):
        for row in self.grid:
            print(' | '.join(row))
            print('-' * (self.size * 4 - 1))

class Agent:
    def __init__(self, world):
        self.world = world
        self.pos = (0, 0)
        self.gold_collected = False
        self.dead = False

    def move(self, direction):
        if self.dead or self.gold_collected:
            return
        x, y = self.pos
        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < self.world.size - 1:
            x += 1
        elif direction == "left" and y > 0:
            y -= 1
        elif direction == "right" and y < self.world.size - 1:
            y += 1

        self.pos = (x, y)
        print(f"Agent moved {direction} to {self.pos}")
        self.check_current_cell()

    def check_current_cell(self):
        x, y = self.pos
        cell = self.world.grid[x][y]
        if cell == 'W':
            print("Agent encountered the Wumpus! Game Over.")
            self.dead = True
        elif cell == 'P':
            print("Agent fell into a pit! Game Over.")
            self.dead = True
        elif cell == 'G':
            print("Agent found the gold! You Win!")
            self.gold_collected = True

if __name__ == "__main__":
    world = WumpusWorld(size=4)
    agent = Agent(world)
    world.display_world()

    # Simple interactive gameplay
    while not agent.dead and not agent.gold_collected:
        move = input("Move (up/down/left/right): ").strip().lower()
        if move in ["up", "down", "left", "right"]:
            agent.move(move)
        else:
            print("Invalid move! Try again.")
