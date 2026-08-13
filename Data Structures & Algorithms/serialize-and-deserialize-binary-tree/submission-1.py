# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = ""

        if not root:
            return ""

        stack = []
        stack.append(root)

        while (stack):
            node = stack.pop()

            if node:
                result += str(node.val)
                result += "#"
                stack.append(node.right)
                stack.append(node.left)
            else:
                result += "N#"
                
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split("#")
        index = 0

        def helper():
            nonlocal index
            val = values[index]
            index += 1
            
            if (val == "N"):
                return None
            elif (not val):
                return None

            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()

            return node

        return helper()


