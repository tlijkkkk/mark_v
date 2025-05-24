from typing import List


class Solution:
    def best_time_to_buy_and_sell_stock(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for price in prices:
            lowest = min(lowest, price)
            max_profit = max(max_profit, price - lowest)
        
        return max_profit