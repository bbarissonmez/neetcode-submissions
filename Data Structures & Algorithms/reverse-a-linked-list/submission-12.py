# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        elif head.next is None:
            return head

        curr = head.next
        last = head
        head.next = None

        while (curr is not None):
            next_stop = curr.next
            curr.next = last
            last = curr
            curr = next_stop        

        return last

