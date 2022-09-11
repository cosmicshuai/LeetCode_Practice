from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = []
        for i in range(n):
            candidates.append((efficiency[i], speed[i]))

        candidates.sort(reverse=True)

        score = 0
        queue = []
        ans = 0
        for e, s in candidates:
            score += s
            heapq.heappush(queue, s)
            if len(queue) > k:
                score -= heapq.heappop(queue)
            ans = max(ans , score * e)

        return ans % (10**9 + 7)