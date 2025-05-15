from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for i in coins:
            for j in range(i, len(dp)):
                dp[j] = min(dp[j], dp[j - i] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1