from collections import defaultdict
from typing import List
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
        
        tree = defaultdict(list)
        visited = set()
        def buildTree(node):
            visited.add(node)
            for i in graph[node]:
                if not i in visited:
                    tree[node].append(i)
                    buildTree(i)
        buildTree(0)
        
        self.ans = 0
        def dfs(node):
            if len(tree[node]) == 0:
                return 1, 1
            tp = 1
            for i in tree[node]:
                c, p = dfs(i)
                self.ans += c
                tp += p
            return math.ceil(tp / seats), tp
        dfs(0)
        return self.ans

