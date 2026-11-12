# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(l1, l2, carriedOne):
            if not l1 and not l2 and not carriedOne:
                return None
            elif not l1 and not l2 and carriedOne:
                return ListNode(1)

            if not l1:
                l1 = ListNode()
            elif not l2:
                l2 = ListNode()
                
            partial_sum = l1.val + l2.val

            if carriedOne:
                partial_sum += 1

            carriedOne = False

            if partial_sum >= 10:
                carriedOne = True
                partial_sum %= 10
            
            node = ListNode(partial_sum)
            node.next = dfs(l1.next, l2.next, carriedOne)

            return node

        start_node = dfs(l1, l2, False)
        return start_node


        