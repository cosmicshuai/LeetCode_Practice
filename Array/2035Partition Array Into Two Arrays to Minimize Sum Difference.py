from collections import defaultdict
import bisect
from typing import List

"""
basic idea:
divide the array into two parts with same size,
enumerate all possible combinations in each part,
do a binary search on the second part
"""
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def dfs(idx, cur, cnt, arr, mem):
            if idx == len(arr):
                mem[cnt].append(cur)
                return 
            dfs(idx + 1, cur, cnt, arr, mem)
            dfs(idx + 1, cur + arr[idx], cnt + 1, arr, mem)
        
        s1 = defaultdict(list)
        s2 = defaultdict(list)        
        
        n = len(nums) // 2
        dfs(0, 0, 0, nums[0:n], s1)
        dfs(0, 0, 0, nums[n::], s2)
        tot = sum(nums)
        half = tot // 2
        ans = abs(sum(nums[0:n]) -  sum(nums[n::]))
        
        for l in range(1, n):
            r = n - l
            left = s1[l]
            right = s2[r]
            right.sort()
            for v in left:
                target = half - v 
                idx = bisect.bisect_left(right, target)
                if idx < len(right):
                    ans = min(ans, abs((v + right[idx]) * 2 - tot))
                if idx > 0:
                    ans = min(ans, abs((v + right[idx- 1]) * 2 - tot))
                    
        return ans