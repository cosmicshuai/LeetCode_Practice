from typing import List


class Solution:
        """
        Do not return anything, modify board in-place instead.
        """
        def solveSudoku(self, board: List[List[str]]) -> None:
            cnt = 0
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        cnt += 1

            def isValid(i, j, v):
                for k in range(9):
                    if board[i][k] == v:
                        return False
                    if board[k][j] == v:
                        return False
                
                bx = i // 3
                by = j // 3
                sx = bx * 3
                sy = by * 3
                for k in range(3):
                    for l in range(3):
                        if board[sx + k][sy + l] == v:
                            return False
                return True
            
            def dfs(board):
                if cnt == 0:
                    return True
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == ".":
                            for k in range(1, 10):
                                if isValid(i, j, str(k)):
                                    board[i][j] = str(k)
                                    if dfs(board):
                                        return True
                                    else:
                                        board[i][j] = "."
                            return False

                return True
            dfs(board)