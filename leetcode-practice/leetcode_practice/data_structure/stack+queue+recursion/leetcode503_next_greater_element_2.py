from typing import List

from sortedcontainers import SortedDict


class Solution:
    def next_greater_element_ii(self, nums: List[int]) -> List[int]:
        mono_desc: List[int] = []
        result: List[int] = [-1] * len(nums)

        for i in range(len(nums) * 2):
            idx = i % len(nums)
            while mono_desc and nums[mono_desc[-1]] < nums[idx]:
                result[mono_desc.pop()] = nums[idx]
            mono_desc.append(idx)

        return result

        
            
    
        



        



