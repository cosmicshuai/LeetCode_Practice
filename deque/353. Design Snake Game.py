from collections import deque
from typing import List
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.body = deque([(0, 0)])
        self.m = height
        self.n = width
        self.foods = deque([])
        for x, y in food:
            self.foods.append((x, y))
        self.dirs = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        self.score = 0

    def move(self, direction: str) -> int:
        head = self.body[0]
        x, y = self.dirs[direction]
        nx, ny = head[0] + x, head[1] + y
        if 0 <= nx < self.m and 0 <= ny < self.n:
            if self.foods and (nx, ny) == self.foods[0]:
                self.score += 1
                self.body.appendleft((nx, ny))
                self.foods.popleft()
            else:
                self.body.pop()
                if (nx, ny) in self.body:
                    return -1
                self.body.appendleft((nx, ny))
            return self.score
        else:
            return -1