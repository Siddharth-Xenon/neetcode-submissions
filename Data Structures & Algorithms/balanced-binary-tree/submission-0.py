# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def dfs(root):
            nonlocal balance
            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            print(root.val, lh, rh)
            if abs(rh - lh) > 1:
                balance = False
            return 1 + max(lh, rh)

        dfs(root)
        
        return balance
