import heapq
from typing import List
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        events = []
        for p, g in zip(plantTime, growTime):
            heapq.heappush(events, (-g, p))

        t = 0
        ans = 0
        while events:
            y, x = heapq.heappop(events)
            t += x
            ans = max(ans, t - y)
        return ans