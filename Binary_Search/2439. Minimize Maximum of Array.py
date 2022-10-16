from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        def canForm(k):
            rest = 0
            for i in range(n - 1, 0, -1):
                cur = nums[i]
                if rest + cur <= k:
                    rest = 0
                else:
                    rest = (cur + rest) - k

            return rest + nums[0] <= k

        #binary search: find the first true of canForm
        lo = 0
        hi = max(nums) + 1
        while lo < hi:
            mid = (hi + lo) // 2
            if canForm(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo