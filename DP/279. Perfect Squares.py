import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n + 1):
            t = int(math.sqrt(i))
            for j in range(t, 0, -1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)
        return dp[n]