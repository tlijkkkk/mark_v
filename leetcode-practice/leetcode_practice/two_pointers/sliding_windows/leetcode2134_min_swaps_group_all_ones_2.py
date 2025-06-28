from typing import List

class Solution:
    def min_swaps_group_all_ones_ii(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        if total_ones <= 1:
            return 0

        def get_most(majority: int, win_size: int):
            i = 0
            count = 0
            min_swaps = float('inf')
            for j in range(len(nums)):
                count += 1 if nums[j] == majority else 0

                while j - i + 1 > win_size:
                    count -= 1 if nums[i] == majority else 0
                    i += 1
            
                if j - i + 1 == win_size:
                    min_swaps = min(min_swaps, j - i + 1 - count)
        
            return min_swaps
        
        return min(get_most(1, total_ones), get_most(0, len(nums) - total_ones))

                
