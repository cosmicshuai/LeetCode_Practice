from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mem = {}
        for w in words:
            mem[w] = mem.get(w, 0) + 1
        
        hasSingle = False
        keys = list(mem.keys())

        ans = 0
        for k in keys:
            if k[0] == k[1]:
                ans += (mem[k] // 2) * 4
                if mem[k] % 2 != 0:
                    hasSingle = True
            else:
                if k[::-1] in mem:
                    t = mem[k]
                    q = mem.get(k[::-1], 0)
                    ans += 4 * min(t, q)
                    mem[k] -= min(t, q)
                    mem[k[::-1]] -= min(t, q)
        return ans + 2 if hasSingle else ans