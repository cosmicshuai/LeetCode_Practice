from typing import List
import math
class Solution1:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        mask = 2 **n - 1
        dp = [float('inf')] * (mask + 1)
        dp[mask] = 0
        for i in range(mask, -1, -1):
            for j in range(n):
                if i & (1 << j) != 0 and i - (1 << j) >= 0:
                    gain = n - bin(i).count("1") + 1
                    dp[i - (1 << j)]  = min(dp[i - (1 << j)], dp[i] + math.ceil(power[j] / gain))
        return dp[0]

class Solution2:
    def minimumTime(self, power: List[int]) -> int:
        n = len(power)
        mask = 2 **n - 1
        dp = [float('inf')] * (mask + 1)
        dp[0] = 0
        for i in range(mask + 1):
            for j in range(n):
                gain = bin(i).count("1") + 1
                if i & (1 << j) == 0:
                    dp[i + ( 1<<j )] = min(dp[i + (1 << j)], dp[i] + math.ceil(power[j] / gain))
        
        return dp[mask]



a = [3,4,1]
S = Solution()
print(S.minimumTime(a))