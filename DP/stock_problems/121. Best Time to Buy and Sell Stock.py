from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #size of dp (n + 1) * (num of transcations) * 2
        # dp[i][k][0] means the profits after k transactons on day i, does not hold any stock, 
        dp = [[[float('-inf')] * 2  for _ in range(2)] for _ in range(n + 1)]


        #base condition: on day zero, whatever num of transcations we made, the profit is always 0
        dp[0][1][0] = 0
        #base conditions: if we don't make any transactions, the profit is always 0
        for i in range(n + 1):
            dp[i][0][0] = 0

        for i in range(1, n + 1):
            # on day i the max profit can be obtained by comparing two strategies: 1) do nothing, 2) buy or sell a stock
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i - 1])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i - 1])

        return dp[n][1][0]
        