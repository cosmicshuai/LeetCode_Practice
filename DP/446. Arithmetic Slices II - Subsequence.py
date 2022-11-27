from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = mem[j][diff]
                mem[i][diff] += cnt + 1
                ans += cnt
        return ans
