from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        mem = {}
        for num in changed:
            mem[num] = mem.get(num, 0) + 1
        
        keys = list(mem.keys())
        keys.sort()
        ans = []
        if mem.get(0, 0) > 0:
            if mem.get(0, 0) % 2 == 0:
                ans += [0] * (mem.get(0, 0) // 2)
            else:
                return []
        for i in keys:
            if i == 0:
                continue
            if mem.get(i, 0) > 0:
                print(mem.get(i * 2, 0), mem[i])
                if mem.get(i * 2, 0) >=  mem[i]:
                    mem[i * 2] -= mem[i]
                    ans += [i] * mem[i]
                else:
                    return []
        return  ans

from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        if c[0] % 2 != 0:
            return []
        keys = list(c.keys())
        keys.sort()
        for k in keys:
            if c[k] > c[k *2]:
                return []
            else:
                c[k *2] -= c[k] if k > 0 else c[k] // 2
        return list(c.elements())