from collections import defaultdict, deque
from typing import  List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        union = UnionFind(n+1)
        for x, y in edges:
            union.merge(x, y)
            path[x].append(y)
            path[y].append(x)
        ans = [-1] *(n+1)
        for i in range(1, n+1):
            if ans[i] == -1:
                ans[i] = 0
                q = deque([i])
                while q:
                    p = q.popleft()
                    for newp in path[p]:
                        if ans[newp] == -1:
                            ans[newp] = 1 - ans[p]
                            q.append(newp)
                        elif ans[newp] + ans[p] != 1: return -1
        visited = defaultdict(int)
        for i in range(1, n+1):
            ans[i] = 0
            q = deque([i])
            v = {i}
            cnt = 0
            while q:
                cnt += 1
                for _ in range(len(q)):
                    p = q.popleft()
                    for newp in path[p]:
                        if newp not in v:
                            v.add(newp)
                            q.append(newp)
            visited[union.find(i)] = max(visited[union.find(i)], cnt)
        return sum(visited.values())