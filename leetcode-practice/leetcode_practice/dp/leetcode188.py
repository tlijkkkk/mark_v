from typing import List


class Solution:
    def bestTimeToBuyAndSellStockIV(self, k: int, prices: List[int]) -> int:
        dp: List[List[int]] = [[0] * 2 for _ in range(k)]

        for i in range(k):
            dp[i][0] = -prices[0]
            dp[i][1] = 0

        for i in range(1, len(prices)):
            dp[0][0] = max(dp[0][0], -prices[i])
            dp[0][1] = max(dp[0][1], dp[0][0] + prices[i])
            for j in range(1, k):
                dp[j][0] = max(dp[j][0], dp[j - 1][1] - prices[i])
                dp[j][1] = max(dp[j][1], dp[j][0] + prices[i])

        return dp[-1][1]

