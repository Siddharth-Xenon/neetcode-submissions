# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head
        
        dummy = ListNode()
        dummy.next=head

        fast = head
        slow = head
        i = 1
        while i < n:
            fast = fast.next
            i+=1
        prev = dummy

        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        print(slow.val, fast.val)

        
        prev.next = slow.next
        slow.next = None

        return dummy.next

        

        