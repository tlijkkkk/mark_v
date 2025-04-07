from typing import List


class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        pre_pre = 0
        pre = 0

        for i in range(2, len(cost) + 1):
            current = min(pre_pre + cost[i - 2], pre + cost[i - 1])
            pre_pre = pre
            pre = current
        
        return pre