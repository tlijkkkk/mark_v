from typing import List

class Solution:
    def max_width_ramp(self, nums: List[int]) -> int:
        right_prefix_max: List[int] = [float('-inf')] + [0] * len(nums)

        for j in range(len(nums) - 1, -1, -1):
            right_prefix_max[j] = max(right_prefix_max[j + 1], nums[j])

        max_width = 0
        i = 0
        for j in range(len(nums)):
            while nums[i] > right_prefix_max[j]:
                i += 1

            max_width = max(max_width, j - i)

        return max_width
            