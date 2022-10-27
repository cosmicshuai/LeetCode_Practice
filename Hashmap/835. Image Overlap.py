from collections import defaultdict
from typing import List
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        mem1, mem2 = set(), set()
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    mem1.add((i,j))
                if img2[i][j] == 1:
                    mem2.add((i,j))

        diff = defaultdict(int)
        for i, j in mem1:
            for x, y in mem2:
                t = str(i - x) + ":" + str(j - y)
                diff[t] += 1
        

        ans = 0
        for v in diff.values():
            ans = max(ans, v)
        return ans