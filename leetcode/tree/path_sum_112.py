# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = False

    def hasPathSum(self, root, targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return
            if not node.left and not node.right and curr_sum - node.val == 0:
                print(curr_sum, node.val)
                self.flag = True
                return True
                # last recursion
            dfs(node.left, curr_sum - node.val)
            dfs(node.right, curr_sum - node.val)

        dfs(root, targetSum)
        return self.flag

