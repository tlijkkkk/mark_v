from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        dp_pre = 0
        dp_current = 0
        result = float('-inf')

        for num in nums:
            dp_current = max(dp_pre + num, num)
            result = max(result, dp_current)
            dp_pre = dp_current

        return result