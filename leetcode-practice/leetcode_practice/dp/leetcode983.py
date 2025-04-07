from typing import List


class Solution:
    def min_cost_4_tickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        dp: List[int] = [0] * (max_day + 1)
        days_set = set(days)

        for i in range(1, len(dp)):
            if i in days_set:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0], 
                    dp[max(0, i - 7)] + costs[1], 
                    dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


