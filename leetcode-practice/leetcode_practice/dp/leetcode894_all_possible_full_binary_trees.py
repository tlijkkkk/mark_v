from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def all_possible_full_binary_trees(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []  # Full binary tree must have odd number of nodes

        dp: List[List[TreeNode]] = [[TreeNode(0)]]
        for i in range(1, n // 2 + 1):  # Full binary tree must have equal amount of left vs right nodes plus a root
            dp.append([])
            for j in range(i):
                for left_tree in dp[j]:
                    for right_tree in dp[i - j - 1]:
                        dp[i].append(TreeNode(0, left_tree, right_tree))

        return dp[-1]
    
    