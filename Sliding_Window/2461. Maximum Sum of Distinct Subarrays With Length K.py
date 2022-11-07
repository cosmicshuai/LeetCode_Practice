from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mem = {}
        i = 0
        j = 0
        cur = 0
        ans = 0
        while i < n and j < n:
            while j < n and j - i < k:
                cur += nums[j]
                mem[nums[j]] = mem.get(nums[j], 0) + 1
                j += 1
            if len(mem.keys()) == k:
                ans = max(ans, cur)
            cur -= nums[i]
            mem[nums[i]] -= 1
            if mem[nums[i]] == 0:
                mem.pop(nums[i])
            i += 1
        return ans