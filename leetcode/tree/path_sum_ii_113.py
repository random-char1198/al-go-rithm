# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        res = []

        def dfs(node, cur_sum, tmp):
            if not node:
                return
            if not node.left and not node.right and cur_sum - node.val == 0:
                tmp += [node.val]
                res.append(tmp)
                return
            dfs(node.left, cur_sum - node.val, tmp + [node.val])
            dfs(node.right, cur_sum - node.val, tmp + [node.val])

        dfs(root, targetSum, [])

        return res
