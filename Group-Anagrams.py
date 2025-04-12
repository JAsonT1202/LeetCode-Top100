class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for s in strs:
            key = ''.join(sorted(s))            
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        return list(hashmap.values())
        