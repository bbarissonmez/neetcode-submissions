# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        current = head

        while (current):
            stack.append(current)
            current = current.next

        if not stack:
            return None

        oddIndex = False
        next_node = None
        n = len(stack)

        while len(stack) > n // 2:
            if (oddIndex):
                head.next = next_node
                head = head.next

                oddIndex = False
            else:
                next_node = head.next
                head.next = stack.pop()
                head = head.next

                oddIndex = True

        head.next = None
