import math
from typing import List

"""
Thinking process:
since we need to build a non-decreasing array, so we can think from the end to the begining.
for a specific step, the current num is cur, the previous is prev, we need to split cur to subarray less or equal to prev
says, cur is 35, prev is 6. so the answer is 5,5,6,6,6,6. 
the number of elements is cnt: math.ceil(cur / prev), so we need do (cnt - 1) splits.
the max of min value after split is cur // cnt 
"""
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[n - 1]
        ans = 0
        for i in range(n - 2, -1, -1):
            cur = nums[i]
            cnt = math.ceil(cur / prev)
            ans += (cnt - 1)
            prev = cur // cnt
        return ans