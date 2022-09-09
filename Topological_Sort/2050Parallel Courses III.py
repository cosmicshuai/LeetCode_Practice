from collections import defaultdict, deque
from typing import List
import heapq
"""
Solution 1. 
Kahn's Algorithm and DP
"""
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * (n + 1)
        graph = defaultdict(list)
        for prev, next_ in relations:
            indegree[next_] += 1
            graph[prev].append(next_)
        
        queue = deque([])
        dp = [ 0 ] * (n + 1)
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i - 1]
        
        while queue:
            cur = queue.popleft()
            for nex in graph[cur]:
                indegree[nex] -= 1
                dp[nex] = max(dp[nex], dp[cur] + time[nex - 1])
                if indegree[nex] == 0:
                    queue.append(nex)
                    
        return max(dp)

"""
Solution 1. 
Kahn's Algorithm and Priority Queue
"""
class Solution_Heap:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for prev, next_ in relations:
            indegree[next_] += 1
            graph[prev].append(next_)
        
        canStudy = []
        for i in range(1, n + 1):
            if indegree[i] == 0:
                canStudy.append(i)
        learning = []
        t = 0
        while True:
            while canStudy:
                course = canStudy.pop()
                heapq.heappush(learning, (t + time[course - 1], course))
                
            if learning:
                finish, learned = heapq.heappop(learning)
                t = finish
                for next_ in graph[learned]:
                    indegree[next_] -= 1
                    if indegree[next_] == 0:
                        canStudy.append(next_)
            if not canStudy and not learning:
                return t