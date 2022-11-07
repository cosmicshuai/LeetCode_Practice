import heapq
from typing import List
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        queue = []
        n = len(costs)
        head = 0
        tail = n - 1
        for _ in range(candidates):
            heapq.heappush(queue, (costs[head], head, 1))
            head += 1
        
        for _ in range(candidates):
            if tail < head:
                break
            heapq.heappush(queue, (costs[tail], tail, 2))
            tail -= 1

        ans = 0
        while k > 0:
            c, idx, d = heapq.heappop(queue)
            ans += c
            if d == 1:
                if head <= tail:
                    heapq.heappush(queue, (costs[head], head, 1))
                    head += 1
            else:
                if head <= tail:
                    heapq.heappush(queue, (costs[tail], tail, 2))
                    tail -= 1
            k -= 1
        return ans 