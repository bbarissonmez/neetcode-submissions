# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lower_bound = float("-inf")
        upper_bound = float("inf")

        return self.isValidBSG(root, lower_bound, upper_bound)

    def isValidBSG(self, root: Optional[TreeNode], lower, upper) -> bool:
        if not root:
            return True

        if (root.left and root.left.val >= root.val):
            return False

        if (root.right and root.right.val <= root.val):
            return False

        if (root.val <= lower or root.val >= upper):
            return False
            
        left_bst = self.isValidBSG(root.left, lower, root.val)
        right_bst = self.isValidBSG(root.right, root.val, upper)

        return left_bst and right_bst