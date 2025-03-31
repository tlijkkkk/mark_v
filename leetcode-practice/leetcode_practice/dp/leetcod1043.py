from typing import List


class Solution:
    def partition_array_for_max_sum(self, arr: List[int], k: int) -> int:
        dp: List[int] = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            for j in range(max(i - k + 1, 0), i + 1):
                partition_sum = max(arr[j: i + 1]) * (i - j + 1)
                dp[i + 1] = max(dp[i + 1], dp[j] + partition_sum)

        return dp[-1]


