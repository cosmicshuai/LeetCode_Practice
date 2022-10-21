from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = float('-inf')
        cnt = 0
        i, j = 0, 0
        n = len(nums)
        while i < n and j < n:
            if nums[j] > cur:
                nums[i] = nums[j]
                cur = nums[i]
                cnt = 1
                i += 1
                j += 1
            elif nums[j] == cur and cnt <= 1:
                nums[i] = nums[j]
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1

        return i