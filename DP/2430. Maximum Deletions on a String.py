from functools import lru_cache


class Solution:
    def deleteString(self, s: str) -> int:
        if len(set(list(s))) == 1:
            return len(s)
            
        @lru_cache(None)
        def backtrack(s):
            n = len(s)
            if n == 0:
                return 0
            ans = 1
            for i in range(n//2, 0, -1):
                t = s[0:i]
                if s[i::].startswith(t):
                    ans = max(ans, 1 + backtrack(s[i::]))
            
            return ans

        return backtrack(s)