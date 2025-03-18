# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def houseRobberIII(self, root: Optional[TreeNode]) -> int:
        # No need to check None of root because problem constraint states tree is not empty

        def doRob(root: Optional[TreeNode]) -> List[int]:
            if root == None:
                return [0, 0]
            
            leftDp = doRob(root.left)
            rightDp = doRob(root.right)

            return [root.val + leftDp[1] + rightDp[1], max(
                leftDp[0] + rightDp[0],
                leftDp[0] + rightDp[1],
                leftDp[1] + rightDp[0],
                leftDp[1] + rightDp[1]
            )]
        
        
        return max(doRob(root))