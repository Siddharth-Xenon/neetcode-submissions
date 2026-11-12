# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next=head
        group_next = head
        curr = head
        old = dummy

        while group_next:
            # print("group: ", group_next.val)
            count = 0
            while group_next and count < k:
                group_next = group_next.next
                count+=1

            if count < k:
                break

            list_end= curr
            prev=group_next
            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            old.next = prev
            old= list_end
            # print(curr.val, prev.val, next_node.val, group_next.val, list_end.val) 

        return dummy.next
        