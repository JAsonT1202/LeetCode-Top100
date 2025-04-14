class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        stack = []
        hashmap = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in hashmap.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != hashmap[char]:
                    return False
                stack.pop()

        return not stack
