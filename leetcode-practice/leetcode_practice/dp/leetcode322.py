from typing import List


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for i in range(len(dp)):
            for j in coins:
                if i - j >= 0 and dp[i - j] != float('inf'):
                    dp[i] = min(dp[i], dp[i - j] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1