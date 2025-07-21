from typing import List
from collections import deque


class Solution:
    def next_greater_element_iv(self, nums: List[int]) -> List[int]:
        desc_mono_stk = []
        desc_mono_stk_promoted = []
        results = [-1] * len(nums)

        for i in range(len(nums)):
            temp = deque()
            while desc_mono_stk and nums[desc_mono_stk[-1]] < nums[i]:
                temp.appendleft(desc_mono_stk.pop()) # these are decending ordered indices, so appendleft to maintain the descending order
             
            while desc_mono_stk_promoted and nums[desc_mono_stk_promoted[-1]] < nums[i]:
                results[desc_mono_stk_promoted.pop()] = nums[i] # these are also decending ordered because we check every nums[i]
            
            desc_mono_stk_promoted += temp 
            desc_mono_stk.append(i)
        
        return results
            