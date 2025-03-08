from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFullBinaryTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return [] # Full binary tree must have odd number of nodes

        dp: List[List[TreeNode]] = [[TreeNode(0)]]
        for i in range(1, n // 2 + 1): # Full binary tree must have equally amount of left vs right nodes plus a root
            dp.append([])
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        dp[i].append(TreeNode(0, left, right))

        return dp[-1]

        
