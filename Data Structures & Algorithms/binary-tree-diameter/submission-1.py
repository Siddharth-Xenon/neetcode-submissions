# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            
            return 1 + max(dfs(root.left), dfs(root.right))
        
        
        node = root
        max_dia = 0
        while node:
            lh, rh =  dfs(node.left) , dfs(node.right)
            diameter = lh + rh
            max_dia = max(diameter, max_dia)
            node = node.right if rh >= lh else node.left
        
        return max_dia 