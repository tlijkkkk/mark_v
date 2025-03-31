from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestorOfBST(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        # determine p, q order
        if q.val < p.val:
            tmp = p
            p = q
            q = tmp
      
        def doFind(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
            if root is not None and q.val < root.val:
                return doFind(root.left, p, q)
            
            if root is not None and p.val > root.val:
                return doFind(root.right, p, q)
        
            return root
        
        return doFind(root, p, q)
            

