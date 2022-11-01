class Solution:
    def findBall(self, grid):
        m = len(grid)
        n = len(grid[0])
        locations = [i for i in range(n)]
        for i in range(m):
            row = grid[i]
            cross = [0] * (n+1)
            cross[0] = cross[n] = 1
            for j in range(n):
                if row[j] == 1:
                    cross[j+1] += 1
                else:
                    cross[j] += 1
            for j in range(n):
                if locations[j] == -1:
                    continue
                t = locations[j]
                if row[t] == 1:
                    if cross[t + 1] < 2:
                        locations[j] = t + 1
                    else:
                        locations[j] = -1
                else:
                    if cross[t] < 2:
                        locations[j] = t - 1
                    else:
                        locations[j] = -1
        return locations