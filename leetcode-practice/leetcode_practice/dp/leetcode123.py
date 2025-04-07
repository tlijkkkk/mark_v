from typing import List


class Solution:
    def best_time_to_buy_and_sell_stock_iii(self, prices: List[int]) -> int:
        dp_1: List[int] = [-prices[0], 0]

        dp_2: List[int] = [dp_1[0], dp_1[1]]

        for i in range(1, len(prices)):
            dp_1[0] = max(dp_1[0], -prices[i])
            dp_1[1] = max(dp_1[1], dp_1[0] + prices[i])
            dp_2[0] = max(dp_2[0], dp_1[1] - prices[i])
            dp_2[1] = max(dp_2[1], dp_2[0] + prices[i])

        return dp_2[1]