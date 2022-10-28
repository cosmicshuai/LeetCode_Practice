from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for s in strs:
            t = list(s)
            t.sort()
            mem["".join(t)].append(s)
        ans = []
        for v in mem.values():
            ans.append(v)
        return ans
        