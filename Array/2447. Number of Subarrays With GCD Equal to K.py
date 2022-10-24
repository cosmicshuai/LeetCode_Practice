import math
from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] % k != 0:
                continue
            if nums[i] == k:
                ans += 1
            q = [nums[i]]
            for j in range(i+1, n):
                if nums[j] % k != 0:
                    break
                
                for i in q:
                    if math.gcd(i, nums[j]) == k:
                        ans += 1
                        break
                q.append(nums[j])
        return ans
