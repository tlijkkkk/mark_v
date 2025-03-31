from typing import List


class Solution:
    def min_size_subarray_sum(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        min_len = float('inf')
        sum_so_far = 0

        while j < len(nums):
            sum_so_far += nums[j]
            while sum_so_far >= target:
                min_len = min(min_len, j - i + 1)
                sum_so_far -= nums[i]
                i += 1
            j += 1

        return min_len if min_len != float('inf') else 0