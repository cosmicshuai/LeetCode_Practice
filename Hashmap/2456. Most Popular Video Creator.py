from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        scores = {}
        works = {}
        for c, i, v in zip(creators, ids, views):
            scores[c] = scores.get(c, 0) + v
            if not c in works:
                works[c] = (i, v)
            else:
                pid, pview = works[c]
                if v > pview:
                    works[c] = (i, v)
                elif v == pview and i < pid:
                    works[c] = (i, v)
         
        ans = []
        max_ = 0
        for c, s in scores.items():
            if s > max_:
                ans = [[c, works[c][0]]]
                max_ = s
            elif s == max_:
                ans.append([c, works[c][0]])
        
        return ans