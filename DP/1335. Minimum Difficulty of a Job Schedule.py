from functools import _lru_cache_wrapper
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        @_lru_cache_wrapper(None)
        def jobSchedule(idx, left):
            if n - idx < left:
                return float('inf')
            
            if left == 1:
                return max(jobDifficulty[idx::])
            
            ans = float('inf')
            for i in range(idx + 1, n):
                ans = min(ans, max(jobDifficulty[idx:i]) + jobSchedule(i, left - 1))

            return ans
            
        ans = jobSchedule(0, d)
        return -1 if ans == float('inf') else ans