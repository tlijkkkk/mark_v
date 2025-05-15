from typing import List


class Solution:
    def best_time_to_buy_and_sell_stock_with_cooldown(self, prices: List[int]) -> int:
        dp: List[int] = [-prices[0], 0, 0]
        
        for i in range(1, len(prices)):
            temp = dp[0]

            dp[0] = max(dp[0], dp[1] - prices[i])
            dp[1] = max(dp[1], dp[2])
            dp[2] = temp + prices[i]

        return max(dp[1], dp[2])