class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(2, 1), (1, 2), (1, -2), (-2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1)]
        @lru_cache(None)
        def dfs(x, y, t):
            if t == 0:
                return 1 / 8 ** k
            ans = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    ans += dfs(nx, ny, t - 1)
            return ans
        t = k
        return dfs(row, column, t)
        