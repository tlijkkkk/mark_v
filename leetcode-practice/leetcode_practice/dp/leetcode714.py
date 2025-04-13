from typing import List


class Solution:
    def best_time_buy_sell_stock_trans_fee(self, prices: List[int], fee: int) -> int:
        dp = [-prices[0], 0]

        for price in prices[1::]:
            tmp = dp[0]
            dp[0] = max(dp[0], dp[1] - price)
            dp[1] = max(dp[1], tmp + price - fee)
        
        return dp[1]
