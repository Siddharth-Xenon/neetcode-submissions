# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        p1, p2 = l1, l2
        while p1 or p2:
            add = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            print(add)
            if add > 9:
                mod = add % 10
                carry = (add - mod)//10
                new = ListNode(mod)
                tail.next = new
                tail = tail.next
            else:
                carry = 0  
                new = ListNode(add)
                tail.next = new
                tail = tail.next

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        
        if carry:
            new = ListNode(carry)
            tail.next = new
            tail = tail.next

        return dummy.next

        