# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = set()

    def dfs(self, node):
        if not node:
            return
        else:
            if node.val not in self.s:
                # if not in s, add to hashset
                self.s.add(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

    def isUnivalTree(self, root) -> bool:
        self.dfs(root)
        return len(self.s) == 1
