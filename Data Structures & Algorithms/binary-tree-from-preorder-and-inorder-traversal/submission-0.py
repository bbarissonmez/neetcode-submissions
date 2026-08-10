# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for index, val in enumerate(inorder):
            indices[val] = index

        self.current = 0

        self.inorder = inorder
        self.preorder = preorder
        self.indices = indices

        return self.build(0, len(inorder) - 1)

    def build(self, left, right):
        if left > right:
            return None
        
        root_value = self.preorder[self.current]
        root = TreeNode(root_value)
        root_index = self.indices[root_value]

        self.current += 1

        root.left = self.build(left, root_index - 1)
        root.right = self.build(root_index + 1, right)

        return root






        