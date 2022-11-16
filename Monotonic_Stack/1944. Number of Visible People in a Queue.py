from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        heights[:] = heights[::-1]
        stack = [] # (idx, height)
        ans = [0] * len(heights)
        for i, h in enumerate(heights):
            while stack and h >= stack[-1][1]:
                stack.pop()
                ans[i] += 1
            ans[i] += 1 if stack else 0
            stack.append((i, h))
        return ans[::-1]
