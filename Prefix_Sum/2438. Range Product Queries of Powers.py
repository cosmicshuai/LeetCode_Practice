from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def getPowers(n):
            upper = 32
            ans = []
            while n > 0:
                for i in range(upper, -1, -1):
                    if n >= 2**i:
                        ans.append(2**i)
                        n -= 2**i
                        break
            return ans[::-1]

        products = [1]
        powers = getPowers(n)
        M = 10**9 + 7
        for i in powers:
            products.append(products[-1] * i)
        
        ans = []
        for l, r in queries:
            ans.append((products[r + 1] // products[l]) % M)
        return ans
