# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.traverse(root, ans)
        return ans
        
    def traverse(self, root, ans):
        if root:
            ans.append(root.val)
            self.traverse(root.left, ans)
            self.traverse(root.right, ans)
