from typing import List


class Solution:
    def max_subarray_sum_one_deletion(self, arr: List[int]) -> int:
        dp1 = [arr[0]]
        dp2 = 0
        max_sum = arr[0]

        for num in range(1, len(arr)):
            tmp = dp1
            dp1 = max(dp1, dp1 + num)
            dp2 = max(tmp, dp2 + num)
            max_sum = max(max_sum, max(dp1, dp2))
        
        return max_sum