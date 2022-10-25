from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        dic = {}
        for c in letters:
            dic[c] = dic.get(c, 0) + 1
        
        n = len(words)
        self.ans = 0

        def getCnt(word):
            cnt = {}
            for c in word:
                cnt[c] = cnt.get(c, 0) + 1
            return cnt

        def canForm(cnt):
            for c in cnt.keys():
                if dic.get(c, 0) < cnt[c]:
                    return False
            return True
        
        def subtractCnt(cnt):
            for c in cnt.keys():
                dic[c] = dic[c] - cnt[c]
        
        def addCnt(cnt):
            for c in cnt.keys():
                dic[c] = dic[c] + cnt[c]
        
        def getScore(cnt):
            s = 0
            for c in cnt.keys():
                s += cnt[c] * score[ord(c) - ord("a")]
            return s

        def backtrack(idx, sc):
            if idx == n:
                self.ans = max(self.ans, sc)
                return
    
            cnt = getCnt(words[idx])
            if canForm(cnt):
                subtractCnt(cnt)
                backtrack(idx + 1, sc + getScore(cnt))
                addCnt(cnt)
            
            backtrack(idx + 1, sc)

        backtrack(0, 0)
        return self.ans
            