from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        n = len(arr)
        def backtrack(idx, s):
            if len(s) == len(set(list(s))):
                self.ans = max(self.ans, len(s))
            
            if idx == n:
                return

            backtrack(idx + 1, s + arr[idx])
            backtrack(idx + 1, s)

        backtrack(0, "")
        return self.ans
