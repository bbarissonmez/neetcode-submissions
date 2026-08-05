# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        merge_tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                merge_tail.next = list2
                list2 = list2.next
            else:
                merge_tail.next = list1
                list1 = list1.next

            merge_tail = merge_tail.next

        # Attach whichever list remains
        if (list1 is None and list2 is not None):
            merge_tail.next = list2
        elif (list1 is not None and list2 is None):
            merge_tail.next = list1

        return dummy.next