# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        \\\
        def reverse(node):
            if node is None:
                return
            
            tmp = node.left
            node.left = node.right
            node.right = tmp
        
            reverse(node.left)
            reverse(node.right)
        
        reverse(root)
        return root


        