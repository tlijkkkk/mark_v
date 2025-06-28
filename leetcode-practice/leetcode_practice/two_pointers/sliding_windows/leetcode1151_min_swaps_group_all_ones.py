from typing import List

class Solution:
    def min_swaps_group_all_ones(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        if total_ones <= 1:
            return 0

        most_ones = 0
        count = 0

        i = 0

        for j in range(len(nums)):
            if nums[j]:
                count += 1
            
            if j - i + 1 > total_ones:
                if nums[i]:
                    count -= 1
                i += 1
            
            most_ones = max(most_ones, count)
        
        return total_ones - most_ones