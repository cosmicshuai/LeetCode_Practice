class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def backtrack(left, cur):
            print(left, cur)
            if cur == target:
                return 1
            
            if cur > target:
                return 0

            if left == 0:
                return 0

            ans = 0
            for i in range(1, k + 1):
                ans += backtrack(left - 1, cur + i)
            return ans

        return backtrack(n, 0)

S = Solution()
print(S.numRollsToTarget(1, 6,3))