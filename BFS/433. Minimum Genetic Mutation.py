from collections import deque, defaultdict
from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not end in bank:
            return -1
        
        q = deque([(start, 0)])

        def isValid(gen1, gen2):
            ans = 0
            for i in range(8):
                if gen1[i] != gen2[i]:
                    ans += 1
            return ans == 1

        tot = [start] + bank
        n = len(tot)
        graph = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isValid(tot[i], tot[j]):
                    graph[tot[i]].append(tot[j])
                    graph[tot[j]].append(tot[i])
        seen = set()
        seen.add(start)
        while q:
            l = len(q)
            for _ in range(l):
                cur, step = q.popleft()
                if cur == end:
                    return step
                for mutation in graph[cur]:
                    if not mutation in seen:
                        seen.add(mutation)
                        q.append((mutation, step + 1))
        return -1