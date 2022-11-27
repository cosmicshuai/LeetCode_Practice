from functools import lru_cache


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        primes = ['2', '3', '5', '7']            
        def isValid(c):
            return c in primes
        
        if not isValid(s[0]) or isValid(s[-1]):
            return 0

        @lru_cache(None)
        def backtrack(idx, cnt):
            if cnt == 1 and idx <= n:
                return 1
            
            if idx >= n:
                return 0
            ans = backtrack(idx + 1, cnt)
            if isValid(s[idx]) and not isValid(s[idx - 1]):
                ans += backtrack(idx + minLength, cnt - 1)
            return ans % (10 ** 9 + 7)
        
        return backtrack(minLength, k)