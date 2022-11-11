class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(i) for i in list(str(n))]
        l = len(nums)
        k = -1
        r = -1
        for i in range(l - 1):
            if nums[i] < nums[i+1]:
                k = i
        if k == -1:
            return -1

        for i in range(k+1, l):
            if nums[i] > nums[k]:
                r = i

        nums[k], nums[r] = nums[r], nums[k]
        nums[:] = nums[0:k+1] + nums[k+1::][::-1]
        nums = [str(i) for i in nums]
        ans = int("".join(nums))
        if ans > 2**31 - 1:
            return -1
        else:
            return ans