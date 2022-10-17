from collections import defaultdict, deque
import copy
from typing import List
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        dg = {}
        graph = defaultdict(set)
        tot = sum(nums)
        n = len(nums)
        for s , e in edges:
            dg[s] = dg.get(s, 0) + 1
            dg[e] = dg.get(e, 0) + 1
            graph[s].add(e)
            graph[e].add(s)

        init = []
        for i in range(n):
            if dg.get(i, 0) == 1:
                init.append(i)


        def bfs(target):
            degree = copy.deepcopy(dg)
            vals = copy.deepcopy(nums)
            queue = deque(init)
            while queue:
                cur = queue.popleft()
                degree[cur] = 0
                for p in graph[cur]:
                    if vals[cur] > target:
                        return False
                    elif vals[cur] < target:
                        vals[p] += vals[cur]
                    degree[p] -= 1
                    if degree[p] == 0: # last node
                        return vals[p] == target
                    elif degree[p] == 1:
                        queue.append(p)

        for c in range(min(nums), tot):
            if tot % c == 0 and bfs(c):
                return tot // c - 1
        
        return 0
        