# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Recursive implementation
        
        if not root: return True
        return self.traverse(root.left, root.right)
    
    def traverse(self, left, right):
        if left and right:
            return left.val == right.val and self.traverse(left.right, right.left) and self.traverse(left.left, right.right)
        return left == right
