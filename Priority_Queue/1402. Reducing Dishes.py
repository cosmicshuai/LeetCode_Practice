import heapq
from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        minq = [-i for i in satisfaction]
        heapq.heapify(minq)
        ans = 0
        cur = 0
        acc = 0
        while minq:
            t = -heapq.heappop(minq)
            acc += t
            cur += acc
            ans = max(ans, cur)
        return ans

a = [-1,-8,0,5,-7]

S = Solution()
print(S.maxSatisfaction(a))