from collections import deque
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(mat)
        n = len(mat[0])
        def getConfig(mat):
            return tuple([tuple(i) for i in mat])

        def isZero(mat):
            for i in range(m):
                for j in range(n):
                    if mat[i][j] != 0:
                        return False
            return True

        def flip(i, j, conf):
            conf[i][j] = 1 - conf[i][j]
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    conf[x][y] = 1 - conf[x][y]

        q = deque([[mat, 0]])
        seen = set()
        seen.add(getConfig(mat))

        while q:
            l = len(q)
            for _ in range(l):
                mat, step = q.popleft()
                if isZero(mat):
                    return step
                for i in range(m):
                    for j in range(n):
                        cur = copy.deepcopy(mat)
                        flip(i, j, cur)
                        config = getConfig(cur)
                        if not config in seen:
                            seen.add(config)
                            q.append([cur, step + 1])
        return -1