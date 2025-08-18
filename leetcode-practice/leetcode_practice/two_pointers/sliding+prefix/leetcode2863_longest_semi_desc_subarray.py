from typing import List

class Solution:
    def longest_semi_desc_subarray(self, nums: List[int]) -> int:
        right_prefix_min: List[int] = [0] * len(nums) + [float('inf')]

        for j in range(len(nums) - 1, -1, -1):
            right_prefix_min[j] = min(right_prefix_min[j + 1], nums[j])

        i = 0
        longest = 0
        for j in range(len(nums)):
            while i < j and nums[i] <= right_prefix_min[j]:
                i += 1
            longest = max(longest, j - i + 1)

        return longest

