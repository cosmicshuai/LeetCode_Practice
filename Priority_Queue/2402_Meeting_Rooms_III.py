import heapq
from typing import List
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0] * n
        pq = []
        meetings.sort()
        for i in range(n):
            heapq.heappush(pq, (0, i))
            
        for start, end in meetings:
            candirooms = []
            while pq and pq[0][0] <= start:
                t, room = heapq.heappop(pq)
                heapq.heappush(candirooms, (room, t))
            if not candirooms:
                t, room = heapq.heappop(pq)
            else:
                room, t = heapq.heappop(candirooms)
            cnt[room] += 1
            
            if t <= start:
                heapq.heappush(pq, (end, room))
            else:
                heapq.heappush(pq, (t + end - start, room))
                
            for u, v in candirooms:
                heapq.heappush(pq, (v, u))

        ans = -1
        maxVal = float('-inf')
        for i, v in enumerate(cnt):
            if v > maxVal:
                maxVal = v
                ans = i
        return ans
        