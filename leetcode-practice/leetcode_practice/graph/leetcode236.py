from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowest_common_ancestor_of_bt(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        def do_find(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
            if root is None:
                return None
            
            if root == p or root == q:
                return root  # Only case that returns non-None leaf

            left = do_find(root.left, p, q)
            right = do_find(root.right, p, q)

            if left is not None and right is not None:
                return root
            
            if left is not None:
                return left
            
            if right is not None:
                return right
            
            return None

        return do_find(root, p, q)


