from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            t = abs(i) - 1
            if nums[t] < 0:
                ans.append(abs(i))
            else:
                nums[t] *= -1
        return ans