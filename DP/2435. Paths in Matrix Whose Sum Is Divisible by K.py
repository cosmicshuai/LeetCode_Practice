from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n, M = len(grid), len(grid[0]), 10 ** 9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for t in range(k):
                    ms = (t + grid[i][j]) % k
                    if j > 0: dp[i][j][ms] += dp[i][j - 1][t]
                    if i > 0: dp[i][j][ms] += dp[i-1][j][t]
                    dp[i][j][ms] %= M
        return dp[m - 1][n - 1][0]


class Solution2:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp =[[[-1] * k for _ in range(n)] for _ in range(m)]
        def dfs(i, j, s):
            if i == m - 1 and j == n - 1:
                if (s + grid[i][j]) % k == 0:
                    return 1
                else:
                    return 0
            if dp[i][j][s] != -1:
                return dp[i][j][s]

            ans = 0
            if i + 1 < m:
                ans += dfs(i + 1, j, (s + grid[i][j]) % k)
            if j + 1 < n:
                ans += dfs(i, j + 1, (s + grid[i][j]) % k)
            
            dp[i][j][s] = ans
            return dp[i][j][s] % (10 ** 9 + 7)
        return dfs(0, 0, 0)