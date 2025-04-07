from typing import List

class Solution:
    def best_time_to_buy_and_sell_stock_ii(self, prices: List[int]) -> int:
        dp: List[int] = [-prices[0], 0]

        for i in range(1, len(prices)):
            current: List[int] = [0] * 2
            current[0] = max(dp[0], dp[1] - prices[i])
            current[1] = max(dp[1], dp[0] + prices[i])
            dp = current
        
        return max(current)