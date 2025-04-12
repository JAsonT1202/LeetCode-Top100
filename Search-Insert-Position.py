class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bsearch(left, right):
            if left > right:
                return left
            
            mid = (left + right)/2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return bsearch(mid+1, right)
            else:
                return bsearch(left, mid-1)
        
        return bsearch(0, len(nums)-1)
        

            
        