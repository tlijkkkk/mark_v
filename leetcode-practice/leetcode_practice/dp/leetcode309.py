from typing import List


class Solution:
    def bestTime2BuyNSellStockWithCooldown(self, prices: List[int]) -> int:
        dp: List[int] = [-prices[0], 0, 0]
        
        for i in range(1, len(prices)):
            tmp = dp[0]

            dp[0] = max(dp[0], dp[1] - prices[i])
            dp[1] = max(dp[1], dp[2])
            dp[2] = tmp + prices[i]

        return max(dp[1], dp[2])