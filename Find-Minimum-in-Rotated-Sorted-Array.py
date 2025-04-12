class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bsearch(left,right):
            if left==right:
                return nums[left]
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                return bsearch(mid+1, right)
            else:
                return bsearch(left,mid)
            
        return bsearch(0, len(nums)-1)
