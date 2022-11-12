import math


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0
        M = 10 ** 9 + 7
        for i in range(1, high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
            if i >= low:
                ans += dp[i] % M
        return ans % M

#A TLE Soltion using math.comb
class Solution2:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        def getCntByLen(l):
            cnt0 = l // zero
            cnt = 0
            for i in range(cnt0+1):
                cnt1 = (l - i*zero) // one
                for j in range(cnt1 + 1):
                    cnt += math.comb(i+j, j)
            return cnt

        return (getCntByLen(high) - getCntByLen(low - 1)) % (10**9 + 7)        