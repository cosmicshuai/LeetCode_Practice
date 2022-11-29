from collections import defaultdict
from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        for r, p in richer:
            graph[p].append(r)

        @lru_cache(None)
        def dfs(v):
            ans = v
            q = quiet[v]
            for i in graph[v]:
                p, t = dfs(i)
                if t < q:
                    ans = p
                    q = t
            return ans, q
        ans = []
        for i in range(n):
            p, q = dfs(i)
            ans.append(p)
        return ans
r = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
q = [3,2,5,4,6,1,7,0]
S = Solution()
print(S.loudAndRich(r, q))