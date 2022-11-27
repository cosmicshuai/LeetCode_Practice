from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pos = defaultdict(list)
        m = 9
        for i in range(m):
            for j in range(m):
                if(board[i][j] != "."):
                    pos[board[i][j]].append((i, j))
        def getBoxId(p):
            x = p[0] // 3
            y = p[1] // 3
            return 3 * y + x            
        

        def isValid(p1, p2):
            if p1[0] == p2[0] or p1[1] == p2[1]:
                return False
            
            if getBoxId(p1) == getBoxId(p2):
                return False
            return True

        for key in pos.keys():
            l = len(pos[key])
            for i in range(l - 1):
                for j in range(i+1, l):
                    if not isValid(pos[key][i], pos[key][j]):
                        return False
        return True
