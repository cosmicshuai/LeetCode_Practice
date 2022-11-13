from typing import List
import math

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = 0
        ans = 0
        while i < n:
            j = i + 1
            if nums[i] == k:
                ans += 1
            tmp = nums[i]
            while j < n:
                tmp = math.lcm(tmp, nums[j])
                if tmp == k:
                    ans += 1
                j += 1
            i += 1
        return ans


a = [3,6,2,7,1]
k = 6
S = Solution()
print(S.subarrayLCM(a, k))
