from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        psum = [0]
        for num in nums:
            psum.append(psum[-1] + num)
            
        ans = 1
        i, j = 0, 0
        n = len(nums)
        while i < n and j < n:
            while j < n and (psum[j] - psum[i]) & nums[j] == 0:
                j += 1
                ans = max(ans, j - i)
                    
                while i < n and j < n and (psum[j] - psum[i]) & nums[j] != 0:
                    i += 1
        return ans