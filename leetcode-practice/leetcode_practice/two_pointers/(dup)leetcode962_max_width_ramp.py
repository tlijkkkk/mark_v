from typing import List

class Solution:
    def max_width_ramp(self, nums: List[int]) -> int:
        indices: List[int] = [i for i in range(len(nums))]
        indices.sort(key=lambda i: (nums[i], i))

        min_idx = indices[0]
        max_width = 0

        for i in indices:
            max_width = max(max_width, i - min_idx)
            min_idx = min(min_idx, i)

        return max_width