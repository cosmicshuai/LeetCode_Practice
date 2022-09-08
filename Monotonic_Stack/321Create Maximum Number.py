from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def compare(arr1, arr2):
            if not arr2:
                return True
            if not arr1:
                return False
            if arr1[0] > arr2[0]:
                return True
            elif arr1[0] < arr2[0]:
                return False
            else:
                return compare(arr1[1::], arr2[1::])

        def merge(arr1, arr2):
            if not arr1 or not arr2:
                return arr1 + arr2
            u = len(arr1)
            v = len(arr2)
            ans = []
            i, j = 0, 0
            while i < u or j < v:
                if i == u and j == v:
                    break
                elif i == u:
                    ans.append(arr2[j])
                    j += 1
                elif j == v:
                    ans.append(arr1[i])
                    i += 1
                else:
                    if compare(arr1[i::], arr2[j::]):
                        ans.append(arr1[i])
                        i += 1
                    else:
                        ans.append(arr2[j])
                        j += 1
            return ans
        
        def getMaxKLength(nums, k):
            stack = []
            n = len(nums)
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i] and len(stack) + (n - i) > k: 
                    stack.pop()
                stack.append(i)

            return [nums[i] for i in stack][0:k]
        
        m = len(nums1)
        n = len(nums2)
        ans = []
        maxVal = -1
        for i in range(k + 1):
            j = k - i
            if i > m or j > n:
                continue
            arr1 = getMaxKLength(nums1, i)
            arr2 = getMaxKLength(nums2, j)
            t = merge(arr1, arr2)
            val = int("".join([str(i) for i in t])) 
            if val > maxVal:
                maxVal = val
                ans = t
        return ans

S = Solution()
a = [6,7]
b =[6,0,4]
k = 5
print(S.maxNumber(a, b, k))