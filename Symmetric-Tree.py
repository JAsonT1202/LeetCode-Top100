# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: bool
        \\\
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is None:
                return False
            elif node2 is not None and node1 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return check(node1.left, node2.right) and check(node1.right, node2.left)
        
        return check(root, root)