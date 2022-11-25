from collections import defaultdict
from typing import List

"""
TLE version
"""
class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        self.ans = 0
        graph = defaultdict(list)
        degree = {}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        tree = defaultdict(list)
        visited = [False] * n
        def build_tree(root):
            visited[root] = True
            for child in graph[root]:
                if not visited[child]:
                    tree[root].append(child)
                    build_tree(child)

        build_tree(0)

        def update(arrays):
            n = len(arrays)
            if n < 2:
                return
            for i in range(n - 1):
                for j in range(i + 1, n):
                    for c in arrays[i]:
                        for d in arrays[j]:
                            self.ans = max(self.ans, c ^ d)

        def solve(node):
            if len(tree[node]) == 0:
                return values[node], [values[node]]
            t = values[node]
            subs = []
            newvals = set()    
            for c in tree[node]:
                cur, vals = solve(c)
                t += cur
                subs.append(vals)
                for v in vals:
                    newvals.add(v)
            newvals.add(t)
            update(subs)
            return t, list(newvals)
        
        solve(0)
        return self.ans