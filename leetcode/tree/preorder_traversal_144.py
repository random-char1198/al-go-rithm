# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        res = []

        def traversal(root):
            if root:
                traversal(root.left)
                traversal(root.right)
                res.append(root.val)

        traversal(root)
        return res
