from typing import List

"""
The weighted median optimize the L1 distance
"""
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = list(zip(nums, cost))
        pairs.sort()
        tot = sum(cost)
        cur = 0
        target = 0
        for t, c in pairs:
            cur += c
            if cur >= tot / 2:
                target = t
                break
        return sum([c * abs(target - n) for n, c in pairs])