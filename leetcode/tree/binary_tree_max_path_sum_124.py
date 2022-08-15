# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            curr_path = root.val + left + right

            self.max_sum = max(curr_path, self.max_sum)

            return root.val + max(left, right)

        dfs(root)
        return self.max_sum
