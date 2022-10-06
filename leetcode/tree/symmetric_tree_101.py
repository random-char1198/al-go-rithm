# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        def dfs(left, right):
            # if the structure of the node is wrong then there is no point to proceed
            if not (left or right):
                return True
            # de morgan's law
            # not (a or b) === not a and not b

            if not (left and right):
                return False
            # de morgan's law
            # not (a and b) === not a or not b

            # make ture they are symtraical
            if left.val != right.val:
                return False
            return dfs(left=left.left, right=right.right) and dfs(left=left.right, right=right.left)

        return dfs(left=root.left, right=root.right)
        #     2         2
        #    / \       / \
        #   3   4     4   3
        #  / \ / \   / \ / \
        # 8<-  7 6  5 5  6 7  ->8
        # If 8 ！= 8 in the graph above, just return False
