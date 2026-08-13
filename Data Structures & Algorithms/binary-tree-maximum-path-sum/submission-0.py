class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def maxSum(node) -> int:
            nonlocal max_sum

            # Base case
            if not node:
                return 0

            # Best path we can get from each child
            left_gain = max(0, maxSum(node.left))
            right_gain = max(0, maxSum(node.right))

            # Best COMPLETE path whose highest point is this node
            current_path = (
                node.val
                + left_gain
                + right_gain
            )

            # Update global answer
            max_sum = max(current_path, max_sum)

            # What can we send upward to the parent?
            # Remember: we can only choose ONE branch
            return node.val + max(left_gain, right_gain)

        maxSum(root)

        return max_sum