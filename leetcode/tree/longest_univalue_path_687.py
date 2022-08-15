class Solution:
    def __init__(self):
        self.max_path = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.left:
                left = left + 1 if root.left.val == root.val else 0

            if root.right:
                right = right + 1 if root.right.val == root.val else 0

            self.max_path = max(self.max_path, left + right)
            return max(left, right)

        dfs(root)
        return self.max_path
