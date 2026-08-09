# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        self._push_left_descendants(root, stack)
        result = -1

        for _ in range (k):
            result = self._next_val(stack)

        return result

    def _push_left_descendants(self, node, stack):
            while node:
                stack.append(node)
                node = node.left        

    def _next_val(self, stack):
        node = stack.pop()
        
        if node.right:
            self._push_left_descendants(node.right, stack)

        return node.val
            
        