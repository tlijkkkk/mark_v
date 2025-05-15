# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def house_robber_iii(self, root: Optional[TreeNode]) -> int:
        # No need to check None of root because problem constraint states tree is not empty

        def do_rob(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return [0, 0]
            
            left_dp = do_rob(root.left)
            right_dp = do_rob(root.right)

            return [root.val + left_dp[1] + right_dp[1], max(
                left_dp[0] + right_dp[0],
                left_dp[0] + right_dp[1],
                left_dp[1] + right_dp[0],
                left_dp[1] + right_dp[1]
            )]
        
        return max(do_rob(root))