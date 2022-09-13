import heapq
from sortedcontainers import SortedList
from typing import List
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        events = []
        max_pos = 0
        for i, [s, e] in enumerate(paint):
            events.append((s, i, 1))
            events.append((e, i, -1))
            max_pos = max(max_pos, e)
        events.sort()
        seen = set()
        queue = []
        n = len(events)
        i = 0
        ans = [0] * len(paint)
        for pos in range(max_pos + 1):
            while i < n and events[i][0] == pos:
                loc, idx, type = events[i]
                if type == 1:
                    heapq.heappush(queue, idx)
                else:
                    seen.add(idx)
                i += 1
            
            while queue and queue[0] in seen:
                heapq.heappop(queue)
                
            if queue:
                ans[queue[0]] += 1
        return ans

class Solution2:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        events = []
        max_pos = 0
        for i, [s, e] in enumerate(paint):
            events.append((s, i, 1))
            events.append((e, i, -1))
            max_pos = max(max_pos, e)
        events.sort()
        ans = [ 0 ] * len(paint)
        n = len(events)
        queue = SortedList()
        i = 0
        for pos in range(max_pos + 1):
            while i < n and events[i][0] == pos:
                _, curIdx, type = events[i]
                if type == 1:
                    queue.add(curIdx)
                else:
                    queue.remove(curIdx)
                i += 1
            
            if queue:
                
                ans[queue[0]] += 1
            
        return ans
