class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def getReverse(k):
            ans = 0
            while k > 0:
                t = k % 10
                k = k // 10
                ans = ans * 10 + t
            return ans
        for i in range(num, num//2 - 1, -1):
            if i + getReverse(i) == num:
                return True
        return False