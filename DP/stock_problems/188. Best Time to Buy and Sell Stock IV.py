from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # construct dp array
        dp = [[[float('-inf')] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

        #base cases
        #1. on day zero, no matter how many transactions we made, the profit is always zero
        for i in range(k + 1):
            dp[0][i][0] = 0

        #2. no matter on which day, if we can only make 0 transactions, the profix is always 0
        for i in range(n + 1):
            dp[i][0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])

        return dp[n][k][0]
        