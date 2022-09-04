import heapq
from typing import List
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        psum = [0]
        for c in runningCosts:
            psum.append(psum[-1] + c)
        
        tot = chargeTimes[0] * runningCosts[0]
        n = len(chargeTimes)
        i, j = 0, 0
        ans = 0
        pq = [(-chargeTimes[0], 0)]
        while i < n and j < n:
            while tot <= budget and j < n:
                ans = max(ans, j - i + 1)
                j += 1
                if j < n:
                    heapq.heappush(pq, (-chargeTimes[j], j))
                    tot = -pq[0][0] + (j - i + 1) * (psum[j+1] - psum[i])
                
            while tot > budget and i < n:
                if i < n:
                    while pq and pq[0][1] < i:
                        heapq.heappop(pq)
                    tot = -pq[0][0] * (j - i + 1) * (psum[j] - psum[i]) if pq else 0
                i += 1
                    
                
        return ans
                
chargeTimes = [3,6,1,3,4]
runningCosts = [2,1,3,4,5]
budget = 25
S = Solution()
print(S.maximumRobots(chargeTimes, runningCosts, budget))