from typing import List

class Solution:
    """
    interate through rows, for each row, scan left to right and right to left to track the local max, comparing left and right to find the max for current row
    
    """
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        score = points[0]
        for i in range(1, m):
            left = [float('-inf')] * n
            right = [float('-inf')] * n
            tmp = [float('-inf')] * n
            for j in range(n):
                if j == 0:
                    left[0] = score[0]
                else:
                    left[j] = max(left[j - 1] - 1, score[j])
            
            for j in range(n - 1, -1, -1):
                if j == n-1:
                    right[n-1] = score[n-1]
                else:
                    right[j] = max(right[j + 1] - 1, score[j])

            for j in range(n):
                tmp[j] = max(left[j], right[j]) + points[i][j]

            score = tmp

        return max(score)

