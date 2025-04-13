class Solution(object):
    def majorityElement(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        max_num = max(hashmap, key=hashmap.get)
        return max_num
        