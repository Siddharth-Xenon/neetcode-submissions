# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        searchq= deque([root])
        size = 1
        res = []
        while searchq:
            
            while size > 0:
                node = searchq.popleft()
                if node.left:
                    searchq.append(node.left)
                if node.right:
                    searchq.append(node.right)
                size-=1
            res.append(node.val)
            size = len(searchq)
        
        return res

        