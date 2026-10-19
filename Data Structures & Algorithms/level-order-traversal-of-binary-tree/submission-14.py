# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        level = 0
        node_level = defaultdict(list)

        queue = deque()
        queue.append((root, level))

        while (queue):
            node, lev = queue.popleft()
            node_level[lev].append(node.val)
            
            if node.left is not None:
                queue.append((node.left, lev+1))
            if node.right is not None:
                queue.append((node.right, lev+1))

        return list(node_level.values())

        