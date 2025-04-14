class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            left[i] = left[i]*right
            right = right * nums[i]
        
        return left
        