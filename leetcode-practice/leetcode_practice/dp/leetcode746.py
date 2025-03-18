from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prePre = 0
        pre = 0

        for i in range(2, len(cost) + 1):
            current = min(prePre + cost[i - 2], pre + cost[i - 1])
            prePre = pre
            pre = current
        
        return pre