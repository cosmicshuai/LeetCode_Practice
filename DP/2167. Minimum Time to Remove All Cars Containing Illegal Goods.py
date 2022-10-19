class Solution:
    """
    transform the problem into: ans = len_of_s + 1s_in_mid - 0s_in_mid
    """
    def minimumTime(self, s: str) -> int:
        p = [1 if i == "1" else -1 for i in s]
        n = len(s)
        dp = [0] * n
        dp[0] = p[0]
        for i in range(1, n):
            dp[i] = min(p[i], dp[i-1] + p[i])
        return n + min(0, min(dp))
