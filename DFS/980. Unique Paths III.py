from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start = (-1, -1)
        end = (-1, -1)
        self.tot = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    self.tot += 1
        
        self.ans = 0
        visited = set()
        visited.add(start)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j, cnt):
            if (i, j) == end and cnt == self.tot:
                self.ans += 1
                return
            
            for dx, dy in dirs:
                x , y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1 and (not (x, y) in visited):
                    visited.add((x, y))
                    dfs(x, y, cnt + 1)
                    visited.remove((x, y))
        dfs(start[0], start[1], 0)
        return self.ans