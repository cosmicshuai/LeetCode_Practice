from functools import lru_cache
from typing import List


class Solution:
    """
    Top down DP
    """
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        @lru_cache(2000)
        def backtrack(i, idx):
            if idx == m:
                return 0
            l = nums[i]
            r = nums[n - 1 - idx + i]
            p = multipliers[idx]
            l1 = l * p + backtrack(i + 1,  idx + 1)
            r1 = r * p + backtrack(i,  idx + 1) 
            return max(l1, r1)
        
        return backtrack(0,  0)