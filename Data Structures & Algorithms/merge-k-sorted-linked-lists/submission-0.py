# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq #heapq.heappush() heapq.heappop()
        dummy = ListNode()
        tail = dummy

        heap = []

        for i, head in enumerate(lists):
            if head is not None:
                heap.append((head.val, i , head))

        heapq.heapify(heap)

        while heap:
            value, i , node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next is not None:
                node_next = node.next
                heapq.heappush(heap, (node_next.val, i , node_next))
        
        return dummy.next
        