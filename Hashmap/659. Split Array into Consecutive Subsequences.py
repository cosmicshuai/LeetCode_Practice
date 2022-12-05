import heapq
from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mem = {}
        for num in nums:
            if not num - 1 in mem:
                q = mem.get(num, [])
                heapq.heappush(q, 1)
                mem[num] = q
            else:
                t = mem[num - 1]
                print(num, t)
                occ = heapq.heappop(t)
                if len(t) == 0:
                    mem.pop(num - 1)
                cur = mem.get(num, [])
                heapq.heappush(cur, occ + 1)
                mem[num] = cur

        for vals in mem.values():
            for v in vals:
                if v < 3:
                    return False
        return True


S = Solution()
a = [1,2,3,3,4,4,5,5]
print(S.isPossible(a))