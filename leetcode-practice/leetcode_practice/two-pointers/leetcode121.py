
from typing import List


class Solution:
    def bestTimeToBuyAndSellStock(self, prices: List[int]) -> int:
        highest = prices[-1]
        max_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            highest = max(highest, prices[i])
            max_profit = max(max, highest - prices[i])
        
        return max_profit