from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i , j = 0 , n - 1
        ans = -1
        diff = 1000000
        while i < j:
            cur = nums[i] + nums[j]
            if cur < k:
                if k - cur < diff:
                    ans = cur
                    diff = k - cur
                i += 1
            else:
                j -= 1
        return ans