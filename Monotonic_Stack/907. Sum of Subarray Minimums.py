from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        M = 10 ** 9 + 7
        for i, num in enumerate(arr):
            while stack and stack[-1][0] > num:
                cur, idx = stack.pop()
                left = idx - stack[-1][1] if stack else idx + 1
                right = i - idx
                ans += (cur * left * right % M)
            stack.append((num, i))
        
        n = len(arr)
        prev = -1
        for v, i in stack:
            ans += v * (i - prev) * (n - i) % M
            prev = i
        return ans % M