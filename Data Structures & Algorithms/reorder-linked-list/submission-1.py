# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return None

        slow ,fast = head, head
        
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        
        curr= slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev, curr = curr, nxt
        
        p2 = prev
        p1 = head
        dum = ListNode()
        dum.next = p1
        while p1 and p2:
            nxt = p1.next
            nxt2 = p2.next
            p1.next = p2
            p2.next = nxt
            p1=nxt
            p2=nxt2
        
        



