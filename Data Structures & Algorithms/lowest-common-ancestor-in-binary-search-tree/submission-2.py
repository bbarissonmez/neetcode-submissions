class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = self.get_path(root, p)
        q_ancestors = self.get_path(root, q)

        lca = root
        for n1, n2 in zip(p_ancestors, q_ancestors):
            if n1 == n2:
                lca = n1
            else:
                break
        return lca

    def get_path(self, root: TreeNode, target: TreeNode):
        curr = root
        path = []

        while curr:
            path.append(curr)
            if curr.val == target.val:
                break
            if curr.val > target.val:
                curr = curr.left
            else:
                curr = curr.right
        return path