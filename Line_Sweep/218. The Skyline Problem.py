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

import heapq
"""

"""
class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        corners = set()
        for l, r, h in buildings:
            corners.add((l, -h, r))
            corners.add((r, 0, 1))
        
        corners = list(corners)
        corners.sort()
        heights = [(0, float('inf'))]
        ans = []
        
        for x, h, r in corners:
            while x >= heights[0][1]:
                heapq.heappop(heights)
            if h < 0:
                heapq.heappush(heights, (h, r))
            
            if not ans or ans[-1][1] != -heights[0][0]:
                ans.append([x, -heights[0][0]])
        return ans