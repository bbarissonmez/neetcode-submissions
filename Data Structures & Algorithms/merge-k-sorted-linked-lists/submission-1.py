# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        i, j = 0, len(lists) - 1
        while (len(lists) != 1):
            if (i >= j):
                i = 0
                j = len(lists) - 1
            result = self.merge2Lists(lists[i], lists[j])
            lists[i] = result
            lists.pop()
            i += 1
            j -= 1

        return result



    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = ListNode()
        merge_tail = dummy 
        while list1 and list2:
            if list1.val > list2.val:
                merge_tail.next = list2
                list2 = list2.next
            else:
                merge_tail.next = list1
                list1 = list1.next

            merge_tail = merge_tail.next

        merge_tail.next = list1 or list2

        return dummy.next