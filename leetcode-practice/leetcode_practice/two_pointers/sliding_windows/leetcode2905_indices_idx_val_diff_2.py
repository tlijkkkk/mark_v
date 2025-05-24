from typing import List


class Solution:
    def find_indices_index_value_diff_ii(self, nums: List[int], index_difference: int, value_difference: int) -> List[int]:
        min_val_idx = 0
        max_val_idx = 0

        for j in range(index_difference, len(nums)):
            i = j - index_difference
            if nums[i] < nums[min_val_idx]:
                min_val_idx = i
            if nums[i] > nums[max_val_idx]:
                max_val_idx = i
            
            if nums[j] - nums[min_val_idx] >= value_difference:
                return [min_val_idx, j]
            
            if nums[max_val_idx] - nums[j] >= value_difference:
                return [max_val_idx, j]
        
        return [-1, -1]