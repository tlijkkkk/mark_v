from bisect import bisect_left
from typing import List


class Solution:
    def find_indices_index_value_diff_ii(self, nums: List[int], index_difference: int, value_difference: int) -> List[int]:
        min_val_idx = 0
        max_val_idx = 0

        for i in range(index_difference, len(nums)):
            j = i - index_difference
            if nums[j] < nums[min_val_idx]:
                min_val_idx = j
            if nums[j] > nums[max_val_idx]:
                max_val_idx = j
            
            if nums[i] - nums[min_val_idx] >= value_difference:
                return [min_val_idx, i]
            
            if nums[max_val_idx] - nums[i] >= value_difference:
                return [i, max_val_idx]
        
        return [-1, -1]