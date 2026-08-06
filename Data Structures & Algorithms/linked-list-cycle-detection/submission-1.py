# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        elems = set()

        if (head is None):
            return False

        while (head is not None):
            if head in elems:
                return True
            else:
                elems.add(head)
                head = head.next

        return False

        