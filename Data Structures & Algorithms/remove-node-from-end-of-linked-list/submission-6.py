# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (not head.next):
            return None

        count = 0
        current = head
        while (current):
            count += 1
            current = current.next

        index_to_del = count - n

        prev = None
        dummy = head

        for _ in range (index_to_del):
            prev = dummy
            dummy = dummy.next

        if (index_to_del == 0):
            return head.next
            
        prev.next = dummy.next
        return head
        