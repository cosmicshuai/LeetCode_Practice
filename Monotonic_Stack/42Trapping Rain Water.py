from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        n = len(height)
        for h in height:
            if h > leftMax[-1]:
                leftMax.append(h)
            else:
                leftMax.append(leftMax[-1])

        rightMax = [0]
        for i in range(n -1, -1, -1):
            h = height[i]
            if h > rightMax[-1]:
                rightMax.append(h)
            else:
                rightMax.append(rightMax[-1])        
        rightMax = rightMax[::-1]
        print(leftMax, rightMax)
        ans = 0
        for i in range(n):
            ans += max(0, min(leftMax[i], rightMax[i]) - height[i])
        return ans


class Solution2:
    def trap(self, height: List[int]) -> int:
        ans = 0
        curMax = 0
        stack = []
        for i, h in enumerate(height):
            while stack and stack[-1][0] <= h:
                v, idx = stack.pop()
                width = idx - stack[-1][1] if stack else 0
                ans += (min(curMax, h) - v) * width
            curMax = max(curMax, h)
            stack.append((h, i))
        return ans
        

S = Solution()
a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(S.trap(a))