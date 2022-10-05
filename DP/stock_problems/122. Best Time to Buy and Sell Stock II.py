from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # this problem is equivalent to we can make infinite transactions
        dp = [[float('-inf')] * 2 for _ in range(n + 1)]

        # base cases
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])
        
        return dp[n][0]