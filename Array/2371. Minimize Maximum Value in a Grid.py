from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        arr = []
        loc = {}
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
                loc[grid[i][j]] = (i, j)
        arr.sort()
        row = {i:0 for i in range(m)}
        col =  {i:0 for i in range(n)}

        for num in arr:
            x, y = loc[num]
            ans[x][y] = max(row[x], col[y]) + 1
            row[x] = ans[x][y]
            col[y] = ans[x][y]
        return ans