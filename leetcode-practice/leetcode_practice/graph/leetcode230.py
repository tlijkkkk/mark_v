from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kth_smallest_element_in_bst(self, root: Optional[TreeNode], k: int) -> int:
        kth_smallest = -1
        count = 0

        def do_dfs(root: Optional[TreeNode], k: int) -> None:
            nonlocal kth_smallest
            if kth_smallest != -1:
                return

            if root == None:
                return
            
            do_dfs(root.left, k)
            nonlocal count 
            count += 1

            if count == k: 
                kth_smallest = root.val
            
            do_dfs(root.right, k)
        
        do_dfs(root, k)
        return kth_smallest