from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, n = 0, 0, len(nums)
        cur = -101
        while i < n and j < n:
            if nums[j] <= cur:
                j += 1
            else:
                nums[i] = nums[j]
                cur = nums[i]
                i += 1
                j += 1

        return i