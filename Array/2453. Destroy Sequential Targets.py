from collections import defaultdict
from typing import List
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        residual = defaultdict(list)
        for num in nums:
            t = num % space
            residual[t].append(num)
        ans = float('inf')
        cnt = 0
        for v in residual.values():
            t = min(v)
            l = len(v)
            if l > cnt:
                ans = t
                cnt = l
            elif l == cnt and t < ans:
                ans = t
        return ans