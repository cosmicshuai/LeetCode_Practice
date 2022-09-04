from typing import List

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m = len(mat)
        n = len(mat[0])
        self.ans = 0
        def getCovered(mask):
            config = bin(mask)[2::][::-1]
            selectedCols = []
            for i, v in enumerate(config):
                if v == "1":
                    selectedCols.append(i)
            cnt = m
            for i in range(m):
                for j in range(n):
                    if j in selectedCols:
                        continue
                    if mat[i][j] == 1:
                        cnt -= 1
                        break
            return cnt
        
        # use bit masking to represent which rows are selected
        def backtrack(idx, mask):
            if bin(mask).count("1") == cols:
                self.ans = max(self.ans, getCovered(mask))
                return
            if idx == n:
                return
            # select row idx
            backtrack(idx + 1, mask ^ 1 << idx)
            # do not select row idx
            backtrack(idx + 1, mask)
        
        backtrack(0, 0)
        return self.ans

