import bisect
from typing import List      
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        numsdiff = []
        n = len(nums1)
        for i in range(n):
            numsdiff.append(nums1[i] - nums2[i])

        tmp = []
        ans = 0
        for i in range(n):
            ans += bisect.bisect_right(tmp, numsdiff[i] + diff)
            bisect.insort_right(tmp, numsdiff[i])

        return ans