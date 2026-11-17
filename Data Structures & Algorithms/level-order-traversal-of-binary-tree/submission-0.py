# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        from collections import deque
        searchq= deque([root])
        size = 1
        res = []
        temp = []
        while searchq:
            
            while size > 0:
                node = searchq.popleft()
                if node.left:
                    searchq.append(node.left)
                if node.right:
                    searchq.append(node.right)
                temp.append(node.val)
                size-=1
            size = len(searchq)
            res.append(temp)
            temp = []
        
        return res

        