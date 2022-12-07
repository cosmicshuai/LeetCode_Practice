class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [(1, 0),  (-1, 0), (0, 1), (0, -1)]
        def isValidStart(x, y, dx, dy):
            i = x - dx
            j = y - dy
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "#":
                return True
            return False

        def bfs(x, y):
            xcopy = x
            ycopy = y
            for dx, dy in dirs:
                x = xcopy
                y = ycopy
                if not isValidStart(x, y, dx, dy):
                    continue
                t = ""
                i = 0
                while 0 <= x < m and 0 <= y < n:
                    if board[x][y] == "#":
                        break
                    if i == len(word):
                        t += board[x][y]
                    elif board[x][y] == " " or board[x][y] == word[i]:
                        t += word[i]
                        i += 1
                    else:
                        t += board[x][y]
                    
                    x += dx
                    y += dy
                if t == word:
                    return True
            return False


        for i in range(m):
            for j in range(n):
                if bfs(i, j):
                    return True

        return False