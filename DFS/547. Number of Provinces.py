from collections import defaultdict
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vistited = [False] * n
        graph = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)


        def dfs(node):
            vistited[node] = True
            for nx in graph[node]:
                if not vistited[nx]:
                    dfs(nx)
        ans = 0
        for i in range(n):
            if not vistited[i]:
                print(i)
                ans += 1
                dfs(i) 
        return ans           