from functools import lru_cache
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)
        #Why we sort here? Because, it is optimal each robot go to their nearest factory first
        robot.sort()
        factory.sort()
        @lru_cache(None)
        def backtrack(idx, fi, cnt):
            if idx == n:
                return 0
            if fi == m:
                return float('inf')
            
            c1 = backtrack(idx, fi + 1, 0)
            c2 = backtrack(idx + 1, fi, cnt + 1) + abs(factory[fi][0] - robot[idx]) if factory[fi][1] > cnt else float('inf')
            return min(c1, c2)

        return backtrack(0, 0, 0)