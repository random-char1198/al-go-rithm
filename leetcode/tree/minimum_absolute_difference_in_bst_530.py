# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
        self.min_diff = 10000

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return
            self.arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        self.arr = sorted(self.arr)
        for i in range(len(self.arr)):
            for j in range(i + 1, len(self.arr)):
                self.min_diff = min(self.min_diff, abs(self.arr[i] - self.arr[j]))
        return self.min_diff


# -------------- Time Limit Exceeded
# Use in-order iteration to avoid using sorted()
# Must use one for loop


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
        self.min_diff = 10000

    def getMinimumDifference(self, root) -> int:

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        dfs(root)
        self.arr = sorted(self.arr)
        for i in range(len(self.arr) - 1):
            self.min_diff = min(self.min_diff, abs(self.arr[i] - self.arr[i + 1]))
        return self.min_diff
