# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        if head.next is None:
            return False

        slow_pointer = head
        fast_pointer = head

        while (slow_pointer is not None and fast_pointer is not None):
            slow_pointer = slow_pointer.next

            fast_pointer = fast_pointer.next
            if (fast_pointer is not None):
                fast_pointer = fast_pointer.next
            else:
                return False

            if (slow_pointer == fast_pointer):
                return True

        return False

        

        