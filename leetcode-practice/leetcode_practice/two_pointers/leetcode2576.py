from typing import List


class Solution:
    def find_max_num_marked_indices(self, nums: List[int]) -> int:
        nums.sort()
        nums_sorted = sorted(nums)
        i = 0
        j = len(nums_sorted) // 2
        count = 0

        while i < len(nums_sorted) // 2 and j < len(nums_sorted):
            if nums_sorted[i] * 2 <= nums_sorted[j]:
                count += 1
                i += 1
            j += 1
            
        return count * 2
        
