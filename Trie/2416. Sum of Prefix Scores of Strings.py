from collections import defaultdict
from typing import List

class Trie():
    def __init__(self):
        self.children = defaultdict(Trie)
        self.cnt = 0
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
                node.cnt += 1
        ans = []
        for word in words:
            tmp = 0
            node = root
            for char in word:
                node = node.children[char]
                tmp += node.cnt
            ans.append(tmp)

        return ans