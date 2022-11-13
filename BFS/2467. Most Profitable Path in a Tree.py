from collections import defaultdict, deque
from typing import List
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        #state: (alice_loc, bob_loc, alice_income)

        graph = defaultdict(list)
        parent = {}
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        tree = defaultdict(list)
        parent = {}
        visited = set()
        def dfs(node):
            visited.add(node)
            for nex in graph[node]:
                if not nex in visited:
                    tree[node].append(nex)
                    parent[nex] = node
                    dfs(nex)
        dfs(0)
        q = deque([(0, amount[0])])
        amount[bob] = 0
        ans = float('-inf')
        while q:
            bob = parent[bob] if bob != 0 else 0
            l = len(q)
            for _ in range(l):
                ali_loc, ali_inc = q.popleft()
                # judge if alice reach left:
                if len(tree[ali_loc]) == 0:
                    ans = max(ans, ali_inc)
                else:
                    for ali_next in tree[ali_loc]:
                        if ali_next == bob:
                            q.append((ali_next, ali_inc + amount[ali_next] // 2))
                        else:
                            q.append((ali_next, ali_inc + amount[ali_next]))
            amount[bob] = 0
        return ans   