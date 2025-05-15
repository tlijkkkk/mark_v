from typing import List

from sortedcontainers import SortedDict


class Solution:
    def next_greater_element_ii(self, nums: List[int]) -> List[int]:
        desc_mono_stack = []
        result = [0] * len(nums)

        for i in range(2 * len(nums) - 1, -1, -1): # iterate backword
            idx = i % len(nums)
            while desc_mono_stack and nums[desc_mono_stack[-1]] <= nums[idx]:
                desc_mono_stack.pop()

            if not desc_mono_stack:
                result[idx] = -1    
            else:
                result[idx] = nums[desc_mono_stack[-1]]
            desc_mono_stack.append(idx)

        return result
            
    
        



        



