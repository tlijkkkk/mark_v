from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestorOfBT(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        def doFind(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
            if root is None:
                return None
            
            if root == p or root == q:
                return root # Only case that returns non-None leaf

            left = doFind(root.left, p, q)
            right = doFind(root.right, p, q)

            if left is not None and right is not None:
                return root
            
            if left is not None:
                return left
            
            if right is not None:
                return right
            
            return None

        return doFind(root, p, q)            
            
            
