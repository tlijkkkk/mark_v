from typing import List


class Solution:
    def partition_array_for_max_sum(self, arr: List[int], k: int) -> int:
        dp: List[int] = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            for j in range(max(i - k, -1), i):
                partition_sum = max(arr[j + 1: i + 1]) * (i - j)
                dp[i + 1] = max(dp[i + 1], dp[j + 1] + partition_sum)

        return dp[-1]