# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: List[int]
        \\\
        result = []
        def order(node):
            if node is None:
                return
            
            order(node.left)
            result.append(node.val)
            order(node.right)
        
        order(root)
        return result

        