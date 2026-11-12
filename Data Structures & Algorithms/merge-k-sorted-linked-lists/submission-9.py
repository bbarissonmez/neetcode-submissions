# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        n = len(lists)
        if n == 1:
            return lists[0]
        left = 0
        right = n-1
        mid = left + (right - left) // 2

        left_half = self.mergeKLists(lists[left:mid+1])
        right_half = self.mergeKLists(lists[mid+1:right+1])

        return self.mergeTwoLists(left_half, right_half)
        
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        elif not list1 and not list2:
            return None

        dummy = ListNode()
        start = dummy

        while (list1 or list2):
            a = list1.val if list1 else float('inf')
            b = list2.val if list2 else float('inf')

            if a < b:
                dummy.next = ListNode(a)
                list1 = list1.next
            else:
                dummy.next = ListNode(b)
                list2 = list2.next

            dummy = dummy.next

        return start.next
