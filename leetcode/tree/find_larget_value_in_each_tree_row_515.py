# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        res = []
        def dfs(curr,curHeight):
            if not curr:
                return
            if curHeight == len(res):
                res.append(curr.val)
            else:
                res[curHeight] = max(res[curHeight],curr.val)
            dfs(curr.left, curHeight + 1)
            dfs(curr.right, curHeight + 1)
        dfs(root,0)
        return res

