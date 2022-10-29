from copy import deepcopy
from agent import Agent


class State:
    cave = []
    original_cave = []
    agent = Agent()
    generation = 0
    score = 1000

    def next_generation(self):
        self.cave = [
            ["s", " ", "b", "p"],
            ["w", "tsb", "p", "b"],
            ["s", " ", "b", " "],
            [" ", "b", "p", "b"],
        ]
        self.cave.reverse()
        self.original_cave = deepcopy(self.cave)
        self.score -= 2
        self.generation += 1
        self.agent.x, self.agent.y = 0, 0
        self.update_map()

    def update_map(self):
        x, y = self.agent.position()
        self.cave = deepcopy(self.original_cave)
        ma = self.cave[y]
        ma[x] = "a"
