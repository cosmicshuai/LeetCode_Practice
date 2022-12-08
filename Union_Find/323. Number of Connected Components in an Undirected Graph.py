from typing import List

class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
    
    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.parent[a]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for s, e in edges:
            if uf.find(s) != uf.find(e):
                uf.merge(s, e)
        ans = set()
        for i in range(n):
            ans.add(uf.find(i))
        
        return len(ans)


a = [[5,6],[0,2],[1,7],[5,9],[1,8],[3,4],[0,6],[0,7],[0,3],[8,9]]
n = 10
S = Solution()
print(S.countComponents(n, a))