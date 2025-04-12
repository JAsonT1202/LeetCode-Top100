class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bsearch1(left, right):
            if left > right:
                return -1
            mid = (left+right)//2
            if target == nums[mid]:
                x = bsearch1(left, mid-1)
                return x if x!=-1 else mid
            elif target > nums[mid]:
                return bsearch1(mid+1, right)
            else:
                return bsearch1(left, mid-1)
        
        def bsearch2(left, right):
            if left > right:
                return -1
            mid = (left+right)//2
            if target == nums[mid]:
                x = bsearch2(mid+1,right)
                return x if x!=-1 else mid
            elif target > nums[mid]:
                return bsearch2(mid+1, right)
            else:
                return bsearch2(left, mid-1)   

        return [bsearch1(0,len(nums)-1), bsearch2(0,len(nums)-1)]     