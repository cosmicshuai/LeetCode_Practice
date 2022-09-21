import bisect
from typing import List
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(idx, cur, arr, s):
            if idx == len(arr):
                s.add(cur)
                return
            dfs(idx + 1, cur, arr, s)
            dfs(idx + 1, cur + arr[idx], arr, s)
        
        s1 = set()
        s2 = set()
        n = len(nums)
        dfs(0, 0, nums[0:n//2], s1)
        dfs(0, 0, nums[n//2::], s2)
        
        s2 = list(s2)
        s2.sort()
        l = len(s2)
        ans = float('inf')
        for i in s1:
            target = goal - i
            idx = bisect.bisect_left(s2, target)
            if idx < l:
                ans = min(ans, abs(s2[idx] - target))
            if idx > 0:
                ans = min(ans, abs(s2[idx - 1] - target))
                
        return ans