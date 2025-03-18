from typing import List


class Solution:
    def minCost4Tickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        dp: List[int] = [0] * (maxDay + 1)
        daysSet = set(days)

        for i in range(1, len(dp)):
            if i in daysSet:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0], 
                    dp[max(0, i - 7)] + costs[1], 
                    dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
            

