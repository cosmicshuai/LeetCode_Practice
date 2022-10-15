import heapq
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @lru_cache(None)
        def backtrack(cur, prev, cnt, left):
            if left < 0:
                return float('inf')
            if cur >= n:
                return 0

            #if cur char equals to prev char
            if s[cur] == prev:
                inc = 0
                if cnt in [1, 9, 99]:
                    inc = 1
                return inc + backtrack(cur + 1, prev, cnt + 1, left)
            else:
                #delete
                delete = float('inf')
                if left > 0:
                    delete = backtrack(cur + 1, prev, cnt, left - 1)
                not_delete = 1 + backtrack(cur + 1, s[cur], 1, left)
                return min(delete, not_delete)

        return backtrack(0, "", 0, k)