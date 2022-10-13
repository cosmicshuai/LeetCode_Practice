from collections import defaultdict
from typing import List

class Solution:
    """
    using bucket sort, we have n - 1 buckets, and put each element to a bucket, we only need to memory the min ans max in each bucket, calculate the diff between two adjacent non-empty 
    buckets
    """
    def maximumGap(self, nums: List[int]) -> int:
        hi, lo, n = max(nums), min(nums), len(nums)
        if n == 1 or hi == lo:
            return 0
        
        if n == 2:
            return hi - lo

        buckets = defaultdict(list)
        for num in nums:
            idx = (num - lo) * (n - 1) // (hi - lo)
            buckets[idx].append(num)
        
        cads = []
        for i in range(n):
            if buckets[i]:
                cads.append((min(buckets[i]), max(buckets[i])))
        ans = 0
        l = len(cads)
        for i in range(l - 1):
            ans = max(ans, cads[i + 1][0] - cads[i][1])
        return ans