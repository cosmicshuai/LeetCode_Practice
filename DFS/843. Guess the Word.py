# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from collections import defaultdict
from typing import Any, List
"""
basic idea: build a hashmap to memorize each words pair overlap count
take the initial guess as the one who has the most overlap with others
each time a guess is taken, we narrow the candidates, using dfs to make further guesses
"""
class Solution:
    def getInfo(self, word1, word2):
        ans = 0
        for i in range(6):
            if word1[i] == word2[i]:
                ans += 1
        return  ans

    def findSecretWord(self, words: List[str], master: Any) -> None:
        mem = {}
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                cnt = self.getInfo(words[i], words[j])
                if words[i] in mem:
                    mem[words[i]][cnt].append(j)
                else:
                    mem[words[i]] = defaultdict(list)
                    mem[words[i]][cnt].append(j)

                if words[j] in mem:
                    mem[words[j]][cnt].append(i)
                else:
                    mem[words[j]] = defaultdict(list)
                    mem[words[j]][cnt].append(i)

        init = words[0]
        score = 0
        for w in words:
            t = 0
            for k in mem[w].keys():
                t += k * len(mem[w][k])
            if t > score:
                score = t
                init = w

        seen = set()
        candies = set(words)
        def guess(word, candies):
            seen.add(word)
            score = master.guess(word)
            if score == 6:
                return True
            newCandies = set()
            for k in mem[word][score]:
                if words[k] in candies:
                    newCandies.add(words[k])
            candies = newCandies
            for w in candies:
                if not w in seen:
                    if guess(w, candies):
                        return True

            return False
        
        guess(init, candies)