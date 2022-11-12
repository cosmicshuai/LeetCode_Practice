import heapq
class MedianFinder:

    def __init__(self):
        self.cnt = 0
        self.first = []
        self.second = []
        self.median = -1

    def addNum(self, num: int) -> None:
        if not self.first or num <= -self.first[0]:
            heapq.heappush(self.first, -num)
        else:
            heapq.heappush(self.second, num)
            cur = heapq.heappop(self.second)
            heapq.heappush(self.first, -cur)
        self.cnt += 1
        if self.cnt % 2 != 0:
            while len(self.first) > self.cnt // 2 + 1:
                cur = -heapq.heappop(self.first)
                heapq.heappush(self.second, cur)
            self.median =  -self.first[0]
        else:
            while len(self.first) > self.cnt // 2:
                cur = -heapq.heappop(self.first)
                heapq.heappush(self.second, cur)
            self.median = 0.5 * (-self.first[0] + self.second[0])

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()