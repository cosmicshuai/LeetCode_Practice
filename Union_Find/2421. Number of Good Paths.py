from collections import defaultdict, deque
from typing import List
class Union_Find:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        #Dump state to reduce complexity
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        n = len(vals)
        degree = defaultdict(dict)
        for i, v in enumerate(vals):
            degree[i][v] = 1
        uf = Union_Find(n)
        nodes = [(vals[i], i) for i in range(n)]
        nodes.sort()
        ans = n
        for val, cur in nodes:
            for neigh in graph[cur]:
                root_cur, root_neigh = uf.find(cur), uf.find(neigh)
                if vals[neigh] <= val and root_cur != root_neigh:
                    uf.parent[root_cur] = root_neigh
                    ans += degree[root_cur][val] * degree[root_neigh].get(val, 0)
                    degree[root_neigh][val] = degree[root_neigh].get(val, 0) + degree[root_cur][val] 
            
        return ans