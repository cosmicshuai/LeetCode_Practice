from typing import List

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        if nums[0] != 1:
            dp[1] = 1 
        for i in range(1, n):
            for j in range(i):
                if math.gcd(nums[i], nums[j]) > 1:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)
                else:
                    if nums[i] != 1:
                        dp[i + 1] = min(dp[i + 1], dp[i] + 1)       
        return dp[n] if dp[n] < float('inf') else -1