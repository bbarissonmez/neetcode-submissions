class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes
        node = head
        for _ in range(k):
            if not node:
                return head
            node = node.next

        # Reverse k nodes
        prev = None
        curr = head

        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        

        # Connect to the next reversed group
        head.next = self.reverseKGroup(curr, k)

        return prev