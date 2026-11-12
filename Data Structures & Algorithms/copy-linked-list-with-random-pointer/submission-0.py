"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copies = {}
        curr = head

        while (curr):
            copy = Node(curr.val, curr.next, curr.random)
            copies[curr] = copy

            curr = curr.next

        deep_copies = list(copies.values())

        for index in range(len(copies)):
            node = deep_copies[index]
            
            if index == len(copies) - 1:
                node.next = None
            else:
                node.next = deep_copies[index + 1]
            
            node.random = copies.get(node.random)

        return deep_copies[0]


        