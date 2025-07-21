from typing import List

class Solution:
    def max_width_ramp(self, nums: List[int]) -> int:
        right_max: List[int] = [0] * len(nums)

        right_max[-1] = nums[-1]

        for j in range(len(nums) - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], nums[j])

        max_width = 0
        i = 0
        for j in range(len(nums)):
            while nums[i] > right_max[j]:
                i += 1

            max_width = max(max_width, j - i)

        return max_width
            