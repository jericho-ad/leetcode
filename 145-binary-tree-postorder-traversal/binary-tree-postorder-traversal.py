# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.traverse(root, ans)
        return ans
    
    def traverse(self, root, ans):
        if root:
            self.traverse(root.left, ans)
            self.traverse(root.right, ans)
            ans.append(root.val)
