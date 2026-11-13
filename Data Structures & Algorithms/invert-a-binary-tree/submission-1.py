# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        if not root:
            return root
        
        def swap(parent):
            temp = parent.left or None
            parent.left = parent.right or None
            parent.right = temp

            return parent
            
        search_queue = deque()
        search_queue.append(root)
        while search_queue:
            node = search_queue.popleft()
            node = swap(node)
            if node.left:
                search_queue.append(node.left)
            if node.right:
                search_queue.append(node.right)


        return root
        