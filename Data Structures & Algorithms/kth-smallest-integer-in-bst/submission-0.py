# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        out = []
        def inorder(node, out):
            nonlocal k
            if not node:
                return
            
            inorder(node.left, out)
            out.append(node.val)
            inorder(node.right, out)
        
        inorder(root, out)
        return out[k-1]


        