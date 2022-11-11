from typing import List

import heapq
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n
        prev = [[] for _ in range(n)]
        for i, v in enumerate(nums):
            while stack and stack[-1][1] < v:
                idx, val = stack.pop()
                prev[i].append(idx)
            stack.append((i, v))
        print(prev)
        pq = []
        for i in range(n):
            while pq and pq[0][0] < nums[i]:
                v, idx = heapq.heappop(pq)
                ans[idx] = nums[i]
            for j in prev[i]:
                heapq.heappush(pq, (nums[j], j))
        return ans

S = Solution()
a = [11,13,15,12,0,15,12,11,9]

print(S.secondGreaterElement(a))