from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[float('-inf')] * 2 for _ in range(3)] for _ in range(n + 1)]

        #base cases
        for i in range(3):
            # on day zero, no matter how many transactions we made, the profit is always 0
            dp[0][i][0] = 0
        
        for i in range(n + 1):
            # on any day, if we don't make any transactions, the profit is always 0
            dp[i][0][0] = 0
        
        for i in range(1, n + 1):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i- 1][k][0], dp[i - 1][k][1] + prices[i - 1])
                dp[i][k][1] = max(dp[i- 1][k][1], dp[i - 1][k - 1][0] - prices[i - 1])

        return dp[n][2][0]