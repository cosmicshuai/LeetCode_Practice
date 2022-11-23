from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        n = len(colsum)
        ans = [[0]*n for _ in range(2)]

        for i in range(n):
            if colsum[i] == 2:
                ans[0][i] = ans[1][i] = 1
                upper -= 1
                lower -= 1
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    ans[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][i] = 1
                    lower -= 1
        if lower != 0 or upper != 0:
            return []
        return ans