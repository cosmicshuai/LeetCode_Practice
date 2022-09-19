from typing import List

class Solution0:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [0] * 32
        n = len(nums)
        ans = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j) > 0:
                    last[j] = i
            ans[i] = max(1, max(last) - i + 1)
        return ans

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def getBits(num):
            bp = bin(num)[2::][::-1]
            res = [0]* 32
            for i, c in enumerate(bp):
                if c == "1":
                    res[i] = 1
            return res
        
        def arraySum(arr1, arr2):
            n = len(arr1)
            for i in range(n):
                arr1[i] += arr2[i]
            return arr1
                
        def arraySub(arr1, arr2):
            n = len(arr1)
            for i in range(n):
                arr1[i] -= arr2[i]
            return arr1
        
        def isMax(arr1, arr2):
            n = len(arr1)
            for i in range(n):
                if arr1[i] == 0 and arr2[i] > 0:
                    return False
            return True
        
        bitInfo = [0]* 32
        for num in nums:
            bits = getBits(num)
            bitInfo = arraySum(bitInfo, bits)
        
        n = len(nums)
        l = 32
        i, j = 0, 1
        windows = getBits(nums[0])
        ans = []
        while i < n:
            while j < n and not isMax(windows, bitInfo):
                bits = getBits(nums[j])
                windows = arraySum(windows, bits)
                j += 1
            ans.append(max(j - i, 1))
            bits = getBits(nums[i])
            bitInfo = arraySub(bitInfo, bits)
            windows = arraySub(windows, bits)
            i += 1
        return ans

S = Solution()
a = [1,0]
print(S.smallestSubarrays(a))