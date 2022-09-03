class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def getDigits(num):
            ans = []
            while num:
                ans.append(num % 10)
                num //= 10
            return ans

        def getDigitCount(idx, cnt, tight, leadingZero, digits):
            if idx == -1:
                return cnt
            if (idx, cnt, tight, leadingZero) in dp and not tight:
                return dp[(idx, cnt, tight, leadingZero)]

            ans = 0
            k = digits[idx] if tight else 9
            for i in range(k + 1):
                nextTight = True if tight and i == digits[idx] else False
                nextZero =  leadingZero and i == 0
                if i == d and (not leadingZero or i != 0):
                    ans += getDigitCount(idx - 1, cnt + 1, nextTight, nextZero, digits)
                else:
                    ans += getDigitCount(idx - 1, cnt, nextTight, nextZero, digits)

            if not tight:
                dp[(idx, cnt, tight, leadingZero)] = ans

            return ans

        hiDigits = getDigits(high)
        loDigits = getDigits(low - 1)
        dp = {}
        hi = getDigitCount(len(hiDigits) - 1, 0, True, True, hiDigits)
        dp = {}
        lo = getDigitCount(len(loDigits) - 1, 0, True, True, loDigits)
        return hi - lo