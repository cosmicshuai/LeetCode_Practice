from typing import List


class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)
        candis = []
        for i in range(n):
            candis.append((tastiness[i], -price[i]))
        
        candis.sort(reverse = True)
        dp = [[[-1] * (maxCoupons + 1) for _ in range(maxAmount + 1)] for _ in range(n)]
        def dfs(idx, amount, coupons):
            if amount < 0 or idx == n:
                return 0
            if dp[idx][amount][coupons] != -1:
                return dp[idx][amount][coupons]
            
            t = candis[idx][0]
            p = -candis[idx][1]
            take_with_coupon = 0
            if coupons > 0 and amount >= p // 2:
                take_with_coupon = t + dfs(idx + 1, amount - p//2, coupons - 1)

            take_without_coupon = 0
            if amount >= p:
                take_without_coupon = t + dfs(idx + 1, amount - p, coupons)

            no_take = dfs(idx + 1, amount, coupons)

            dp[idx][amount][coupons] = max(take_with_coupon, take_without_coupon, no_take)
            return dp[idx][amount][coupons]

        return dfs(0, maxAmount, maxCoupons)