from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        pureCost = {}
        for i, c in enumerate(cost):
            pureCost[c] = i + 1
        
        def convert(t):
            if t == -1:
                return -1
            else:
                return int(t)

        dp = [-1] * (target + 1)
        dp[0] = ""
        for i in range(target + 1):
            for c, d in pureCost.items():
                if i >= c:
                    if dp[i - c] != -1:
                        dp[i] = str(max(convert(dp[i]), convert(str(d) + dp[i - c]), convert(dp[i - c] + str(d))))      
        return dp[target]

S = Solution()
cost = [4,3,2,5,6,7,2,5,5]
target = 5000
print(S.largestNumber(cost, target))