from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        dp: List[int] = [nums[0]] + [0] * (len(nums) - 1)

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)