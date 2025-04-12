class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            req = target - nums[i]

            if req in hashmap:
                return [hashmap[req],i]
            
            hashmap[nums[i]] = i


                    