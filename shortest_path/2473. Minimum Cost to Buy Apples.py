import heapq
from collections import defaultdict
from typing import List
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = defaultdict(list)
        for s, e, c in roads:
            graph[s].append((e, c))
            graph[e].append((s, c))

        def calDis(city):
            dis = [float('inf')] * (n + 1)
            visited = [False] * (n + 1)
            dis[city] = 0
            q = []
            heapq.heappush(q, (0, city))
            while q:
                cost, cur = heapq.heappop(q)
                visited[cur] = True
                for to, d in graph[cur]:
                    if not visited[to]:
                        if cost + d < dis[to]:
                            dis[to] = cost + d
                            heapq.heappush(q, (dis[to], to))
            return dis

        print(calDis(1))
        return []
n = 4
roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]]
appleCost = [56,42,102,301]
k = 2
S = Solution()
S.minCost(n, roads, appleCost, k)