import bisect
from typing import List

"""
treat left and right corner of each building as an event, sort the list.
if meet the a new left corner, determine the max height use bisect.insort_left.
if meet a right corner, we just remove the corresponding left corner of this builidng
"""
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        corners = set()
        for l, r, h in buildings:
            corners.add((l, -h))
            corners.add((r, h))
        
        corners = list(corners)
        corners.sort()
        heights = [0]
        ans = []
        
        for x, h in corners:
            if h < 0:
                bisect.insort_left(heights, h)
            else:
                idx = bisect.bisect_left(heights, -h)
                heights.pop(idx)
            if not ans or ans[-1][1] != -heights[0]:
                ans.append([x, -heights[0]])
        return ans