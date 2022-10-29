from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def canChange(word, target):
            n = len(word)
            if len(target) != n:
                return False

            t = 0
            for i in range(n):
                if word[i] != target[i]:
                    t += 1
            return t <= 2

        ans = []
        for w in queries:
            for t in dictionary:
                if canChange(w, t):
                    ans.append(w)
                    break
        return ans