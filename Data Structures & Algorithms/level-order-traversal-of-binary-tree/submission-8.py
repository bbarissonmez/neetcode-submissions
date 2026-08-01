# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []

        queue = deque()
        queue.append(root)


        while (queue):
            level_array = []
            qLen = len(queue)

            for _ in range(qLen):
                node = queue.popleft()
                level_array.append(node.val)
                
                if (node.left is not None):
                    queue.append(node.left)
                    
                if (node.right is not None):
                    queue.append(node.right)

            results.append(level_array)

        return results



        