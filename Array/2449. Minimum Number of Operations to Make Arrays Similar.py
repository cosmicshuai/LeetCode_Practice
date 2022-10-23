from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        t_odd = []
        t_even = []
        for i in target:
            if i % 2 == 0:
                t_even.append(i)
            else:
                t_odd.append(i)
        t_odd.sort()
        t_even.sort()

        n_odd = []
        n_even = []
        for i in nums:
            if i % 2 == 0:
                n_even.append(i)
            else:
                n_odd.append(i)
        n_odd.sort()
        n_even.sort()

        def calOps(arr1, arr2):
            n = len(arr1)
            ops = 0
            for i in range(n):
                ops += (abs(arr1[i] - arr2[i]) // 2)
            return ops / 2

        ans = 0
        ans += calOps(t_odd, n_odd)
        ans += calOps(t_even, n_even)
        return int(ans)