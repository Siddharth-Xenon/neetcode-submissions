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
        curr = head
        dummy = Node(0, None, None)
        tail = dummy

        val_idx = {} # val : random node address
        ind_add = {}
        idx = 0
        while curr:
            new = Node(curr.val)
            val_idx[curr] = new
            tail.next = new
            tail = tail.next
            curr = curr.next
            idx +=1
        
        curr = head
        

        while curr:
            val_idx[curr].random = val_idx.get(curr.random)
            curr = curr.next

        return dummy.next
        
        