class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def bsearch(left, right):
            if left > right:
                return -1
            mid = (right+left)//2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return bsearch(left, mid-1)
                else:
                    return bsearch(mid+1, right)
            else:
                if nums[mid] < target <= nums[right]:
                    return bsearch(mid+1, right)
                else:
                    return bsearch(left, mid-1)
        
        return bsearch(0, len(nums)-1)
