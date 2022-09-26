
from typing import List

"""
use two dp array to memorize 
"""
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        before = [1] * n
        cur = 0
        prev = float('inf')
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                before[i] = before[i - 1] + 1

        after = [1] * n
        prev = float('inf')
        cur = 0
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                after[i] = after[i + 1] + 1

        ans = []
        for i in range(k, n - k):
            if before[i - 1] >= k and after[i + 1] >= k:
                ans.append(i)
                
        return ans