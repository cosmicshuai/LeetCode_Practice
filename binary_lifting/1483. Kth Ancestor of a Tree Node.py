import math
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.log = math.ceil(math.log2(n))
        self.dp = [[-2] * (self.log + 1) for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        for j in range(1, self.log + 1):
            for i in range(n):
                if self.dp[i][j-1] == -1:
                    self.dp[i][j] = -1
                else:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
        
        print(self.dp)
        self.parent = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        ans = node
        last = self.log
        while k > 0:
            for j in range(last, -1, -1):
                if k >= 2**j:
                    ans = self.dp[ans][j]
                    last = j
                    if ans == -1:
                        return -1
                    k -= 2**j
        return ans

s = TreeAncestor(7, [-1,0,0,1,1,2,2])
print(s.getKthAncestor(3, 1))