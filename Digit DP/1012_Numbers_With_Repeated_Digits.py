class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        dp = {}
        def getSepcialNumCnt(idx, tight, leadingZero, mask, digits):
            if idx == -1:
                # zero is not in consideration
                return 0 if leadingZero else 1
            if (idx, tight, leadingZero, mask) in dp and not tight:
                return dp[(idx, tight, leadingZero, mask)]

            ans = 0
            k = digits[idx] if tight else 9
            for i in range(k + 1):
                nextTight = True if tight and i == digits[idx] else False
                nextZero = True if i == 0 and leadingZero else False
                if leadingZero and i == 0:
                    ans += getSepcialNumCnt(idx - 1, nextTight, nextZero, mask, digits)
                
                elif mask & 1 << i == 0:
                    ans += getSepcialNumCnt(idx - 1, nextTight, nextZero, mask ^ 1 << i, digits)
            if not tight:
                dp[(idx, tight, leadingZero, mask)] = ans
            return ans

        def getDigits(num):
            ans = []
            while num:
                ans.append(num % 10)
                num //= 10
            return ans
        
        digits = getDigits(n)
        return n - getSepcialNumCnt(len(digits) - 1, True, True, 0, digits)