#Link to the problem

# An naive solution based on the author's hints
class MedianFinder():
    def __init__(self):
        self.cnt = 0
        self.arr = [0] * 64

    def getDigit(self, num):
        lo = 0
        hi = 64
        #[0,1,...] find first k so that num <= 2 ** k
        while lo < hi:
            mid = (lo + hi) // 2
            if num <= 2 ** mid:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def addValue(self, val):
        k = self.getDigit(val)
        self.arr[k] += 1
        self.cnt += 1

    def getMedian(self):
        i = 0
        prev = 0
        cur = 0
        mid = self.cnt // 2 + 1 if self.cnt % 2 != 0 else self.cnt // 2
        for i in range(64):
            cur += self.arr[i]
            if prev < mid and cur >= mid:
                return (2**(i - 1) + 2**i) // 2
            prev = cur
        
        

S = MedianFinder()
S.addValue(1)
S.addValue(6)
S.addValue(10)
S.addValue(100000)
S.addValue(1000000000000)
print(S.getMedian())