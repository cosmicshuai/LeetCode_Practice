from typing import List

class Union_Find():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.degree = [1] * n
        self.isAllConnected = False


    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent != v_parent:
            self.parent[v_parent] = u_parent
            self.degree[u_parent] += self.degree[v_parent]
            if self.degree[u_parent] == self.n:
                self.isAllConnected = True




class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = Union_Find(n)
        logs.sort()
        for t, u, v in logs:
            uf.union(u,v)
            if uf.isAllConnected:
                return t
        
        return -1