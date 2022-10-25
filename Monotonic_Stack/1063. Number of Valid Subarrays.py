from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i, num in enumerate(nums):
            while stack and stack[-1][0] > num:
                val, idx = stack.pop()
                ans += (i - idx)
            stack.append((num, i))
        
        n = len(stack) 
        if n > 0:
            end = stack[-1][1]
            for i in range(n):
                ans += (end - stack[i][1] + 1)
        return ans