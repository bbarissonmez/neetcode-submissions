class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current = head

        while current is not None:
            next_node = current.next   # save the rest of the list
            current.next = prev_node   # reverse the pointer
            
            prev_node = current        # move prev forward
            current = next_node        # move current forward

        return prev_node