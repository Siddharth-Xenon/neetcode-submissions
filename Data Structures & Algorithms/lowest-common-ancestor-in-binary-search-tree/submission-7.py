# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from collections import deque
        searchq= deque([root])

        while searchq:
            node = searchq.popleft()
            print("NODE",node.val)
            print("Q", q.val)
            print("P", p.val)
            if node.val <= p.val and node.val >= q.val:
                return node
            if node.val <= q.val and node.val >= p.val:
                return node
            
            if node.left:
                searchq.append(node.left)
            if node.right:
                searchq.append(node.right)




        