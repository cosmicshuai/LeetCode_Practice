from collections import defaultdict
from typing import List
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for p1, p2 in dislikes:
            graph[p1].add(p2)
            graph[p2].add(p1)
        
        flag = [-1] * (n + 1)
        def dfs(i, t):
            if flag[i] == -1:
                flag[i] = t
                for nex in graph[i]:
                    if not dfs(nex, 1 - t):
                        return False
            else:
                if flag[i] != t:
                    return False
            return True


        for i in range(1, n + 1):
            if flag[i] == -1:
                if not dfs(i, 0):
                    print(flag)
                    return False
        return True

d = [[1,2],[1,3],[2,4]]
n = 4
S = Solution()
print(S.possibleBipartition(n, d))