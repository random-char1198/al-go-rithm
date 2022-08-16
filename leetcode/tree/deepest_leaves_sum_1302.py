# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def leaves_sum(self, root, depth) -> int:
        if not root:
            return 0
        if depth == 1:
            return root.val

        return self.leaves_sum(root.left, depth - 1) + self.leaves_sum(root.right, depth - 1)

    def deepestLeavesSum(self, root):
        print(self.sum)
        depth = self.depth(root)
        self.sum = self.leaves_sum(root, depth)
        return self.sum
