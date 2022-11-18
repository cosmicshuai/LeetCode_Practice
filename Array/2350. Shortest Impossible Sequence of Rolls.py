from typing import List

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        step = 1
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                seen.clear()
                step += 1
        return step

"""
my solution
"""
class Solution1:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n = len(rolls)
        def matchSeq(start, num):
            j = start
            while j < n:
                if rolls[j] == num:
                    return j + 1
                else:
                    j += 1
            return j + 1

        seqs = []
        for i in range(1, k + 1):
            seqs.append((0, i))
        step = 1
        while True:
            t = []
            for start, num  in seqs:
                nex = matchSeq(start, num)
                if nex == n + 1:
                    print(start, num)
                    return step
            
                for i in range(1, k + 1):
                    t.append((nex, i))
            step += 1
            seqs = t

a = [4,2,1,2,3,3,2,4,1]
k = 4
S = Solution()
print(S.shortestSequence(a, k))