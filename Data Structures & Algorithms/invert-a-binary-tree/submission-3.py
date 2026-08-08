# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = []
        stack.append(root)

        while (stack):
            node = stack.pop()
            l_node = node.left
            r_node = node.right

            if (l_node and not r_node):
                node.left = None
                node.right = l_node
                stack.append(l_node)
            elif (r_node and not l_node):
                node.right = None
                node.left = r_node
                stack.append(r_node)
            elif (l_node and r_node):
                node.right = l_node
                node.left = r_node
                stack.append(l_node)
                stack.append(r_node)

        return root