from typing import List


class Solution:
    def partitionArray4MaxSum(self, arr: List[int], k: int) -> int:
        dp: List[int] = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            for j in range(max(i - k + 1, 0), i + 1):
                partitionSum = max(arr[j: i + 1]) * (i - j + 1)
                dp[i + 1] = max(dp[i + 1], dp[j] + partitionSum)

        return dp[-1]


