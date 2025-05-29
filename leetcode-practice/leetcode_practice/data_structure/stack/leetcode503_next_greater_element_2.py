from typing import List

from sortedcontainers import SortedDict


class Solution:
    def next_greater_element_ii(self, nums: List[int]) -> List[int]:
        desc_mono_stk = []
        result = [-1] * len(nums)

        for i in range(len(nums) * 2):
            idx = i % len(nums)
            while desc_mono_stk and nums[desc_mono_stk[-1]] < nums[idx]:
                result[desc_mono_stk.pop()] = nums[idx]
            desc_mono_stk.append(idx)

        return result

        
            
    
        



        



