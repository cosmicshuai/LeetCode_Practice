class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def isPalind(i, j):
            j -= 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        @lru_cache(None)
        def backtrack(idx):
            if idx >= n:
                return 0

            ans = backtrack(idx + 1)
            if idx + k <= n and isPalind(idx, idx + k):
                ans = max(ans, 1 + backtrack(idx + k))
            if idx + k + 1 <= n and isPalind(idx, idx + k + 1): # we need this because, if k is odd, then the previous if only consider odd length substring, adding k + 1 to make sure we consider even cases, vice versa
                ans = max(ans, 1 + backtrack(idx + k + 1))
            return ans

        return backtrack(0)