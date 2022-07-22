
class Solution:
    def isValidBST(self, root) -> bool:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True
# inorder traversal it should make the list in ascending order
# Use inorder to traverse the tree and add each item in the tree and check if the list is in ascending order

