from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestElementInBST(self, root: Optional[TreeNode], k: int) -> int:
        kthSmallest = -1
        count = 0

        def doDFS(root: Optional[TreeNode], k: int) -> None:
            nonlocal kthSmallest
            if kthSmallest != -1:
                return

            if root == None:
                return
            
            doDFS(root.left, k)
            nonlocal count 
            count += 1

            if count == k: 
                kthSmallest = root.val
            
            doDFS(root.right, k)
        
        doDFS(root, k)
        return kthSmallest