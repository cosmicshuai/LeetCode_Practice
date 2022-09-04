class Solution:
    def countDigitOne(self, n: int) -> int:
        dp = {}
        def getNumOfDigitOne(idx, cnt, tight, digits):
            if idx == -1:
                return cnt
            
            if (idx, cnt, tight) in dp:
                return dp[(idx, cnt, tight)]
            
            k = digits[idx] if tight else 9
            ans = 0
            for i in range(k + 1):
                nextTight = True if tight and i == digits[idx] else False
                if i == 1:
                    ans += getNumOfDigitOne(idx - 1, cnt + 1, nextTight, digits)
                else:
                    ans += getNumOfDigitOne(idx - 1, cnt, nextTight, digits)

            if not tight:
                dp[(idx, cnt, tight)] = ans
            
            return ans

        def getDigits(num):
            ans = []
            while num:
                ans.append(num % 10)
                num //= 10
            return ans

        digits = getDigits(n)
        return getNumOfDigitOne(len(digits) - 1, 0, True, digits)

S = Solution()
assert S.countDigitOne(1000000000) == 900000001
