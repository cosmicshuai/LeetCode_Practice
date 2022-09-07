from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start = float('inf')
        end = float('-inf')
        n = len(nums)
        for i in range(n):
            prev = []
            if stack and nums[stack[-1]] > nums[i]:
                end = max(end, i)
            while stack and nums[stack[-1]] > nums[i]:
                prev.append(stack.pop())
            if prev:
                start = min(start, prev[-1])
                stack.append(i)
                stack.append(prev[0])
            else:
                stack.append(i)
            
            
            
        return end - start + 1 if start != float('inf') else 0

S = Solution()
a = [2,6,4,8,10,9,15]
print(S.findUnsortedSubarray(a))