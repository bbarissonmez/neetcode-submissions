# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        exists = False
        stack = []

        stack.append(root)

        while (stack):
            node = stack.pop()

            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                exists = True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return exists

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # 0,0 -> True
            return True

        if not p or not q or (p.val != q.val): # 0,1 or 1,0 -> False
            return False

    

        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same
        
        