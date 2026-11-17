# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        
        from collections import deque
        
        def is_same(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return(
                p.val == q.val
                and is_same(p.left, q.left)
                and is_same(p.right, q.right)
            )


        
        
        is_alike = False
        searchq = deque([root])
        while searchq:
            node = searchq.popleft()
            if node.left:
                searchq.append(node.left)
            if node.right:
                searchq.append(node.right)

            if is_same(node, subRoot):
                return True
                
        return False


        