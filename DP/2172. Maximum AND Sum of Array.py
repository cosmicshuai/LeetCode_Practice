from functools import lru_cache
from typing import List

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(idx, mask):
            if idx == n:
                return 0
            ans = 0
            for i in range(numSlots):
                if (mask // 3** i) % 3 > 0:
                    ans = max(ans, dfs(idx + 1, mask - 3 ** i) + (nums[idx] & (i + 1)))  
                    
            return ans
        
        init = 3** numSlots - 1
        return dfs(0, init)
        