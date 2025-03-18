from typing import List


class Solution:
    def bestTimeToBuyAndSellStockIII(self, prices: List[int]) -> int:
        dp1: List[int] = [-prices[0], 0]

        dp2:  List[int] = [dp1[0], dp1[1]]

        for i in range(1, len(prices)):
            dp1[0] = max(dp1[0], -prices[i])
            dp1[1] = max(dp1[1], dp1[0] + prices[i])
            dp2[0] = max(dp2[0], dp1[1] - prices[i])
            dp2[1] = max(dp2[1], dp2[0] + prices[i])

        return dp2[1]