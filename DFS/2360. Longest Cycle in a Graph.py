from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        self.ans = -1
        stack = []
        steps = {}
        def dfs(i):
            visited[i] = True
            stack.append(i)
            steps[i] = len(stack)
            j = edges[i]
            if j != -1 and not visited[j]:
                if dfs(j):
                    return True
            elif j in stack:
                self.ans = max(self.ans, len(stack) - steps[j] + 1)
                return True
            return False
        
        hasCycle = False
        for i in range(n):
            if not visited[i]:
                stack = []
                steps = {}
                hasCycle = dfs(i) or hasCycle
        if not hasCycle:
            return -1
        
        return self.ans

e = [1,2,0,4,5,6,3,8,9,7]
S = Solution()
print(S.longestCycle(e))