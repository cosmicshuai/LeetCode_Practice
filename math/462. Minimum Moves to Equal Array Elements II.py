from typing import List

"""
Use median to minimize the L1 distance
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        median = n // 2  if n % 2 == 1 else n // 2 - 1
        print(nums[median])
        ans = 0
        for num  in nums:
            ans += abs(num - nums[median])

        return ans