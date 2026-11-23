# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        q = deque()
        level = 1
        q.append([root, level])
        
        tree = []

        while (q):
            pack = q.popleft()
            tree.append(pack)

            node, curr_level = pack[0], pack[1]
            if node.left:
                q.append([node.left, curr_level + 1])
            if node.right:
                q.append([node.right, curr_level + 1])

        res = []

        for i in range(len(tree)):
            if tree[i][1] == level + 1:
                res.append(tree[i-1][0].val)
                level += 1

        res.append(tree[-1][0].val)
        return res



            
