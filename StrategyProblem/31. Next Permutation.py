class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = -1
        l = -1
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                k = i
        if k == -1:
            nums[:] = nums[::-1]
            return 

        for i in range(k+1, n):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]
        nums[:] = nums[0:k+1] + nums[k+1::][::-1]