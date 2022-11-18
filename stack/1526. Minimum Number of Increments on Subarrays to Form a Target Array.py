from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        stack = [ 0 ]
        base = 0
        dec = False
        ans = 0
        for num in target:
            if num > stack[-1]:
                if not dec:
                    stack.append(num)
                else:
                    dec = False
                    ans += (max(stack) - base)
                    base = stack[-1]
                    stack = [num]
            elif num < stack[-1]:
                dec = True
                stack.append(num)
            else:
                stack.append(num)
        return ans + max(stack) - base

a = [1,1,5,5,4,3,5,1,1]
S = Solution()
print(S.minNumberOperations(a))