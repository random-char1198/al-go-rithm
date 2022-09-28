# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root) -> list[str]:

        def dfs(node, s):
            if node:
                # if curr node is
                s += str(node.val)
                if not node.left and not node.right:
                    # leaf node
                    # with no left node or right node,
                    # append current path to the list
                    res.append(s)
                else:
                    # continue to traverse and pass the s to the future.
                    s += "->"
                    dfs(node.left, s)
                    dfs(node.right, s)
        res = []
        dfs(root, '')
        return res
