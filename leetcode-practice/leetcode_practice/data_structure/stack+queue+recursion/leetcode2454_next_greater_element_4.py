from typing import List
from collections import deque


class Solution:
    def next_greater_element_iv(self, nums: List[int]) -> List[int]:
        mono_desc: List[int] = []
        mono_desc_promote: List[int] = []
        results: List[int] = [-1] * len(nums)

        for i in range(len(nums)):
            temp = deque()
            while mono_desc and nums[mono_desc[-1]] < nums[i]:
                temp.appendleft(mono_desc.pop()) # these are descending ordered indices, so appendleft to maintain the descending order
             
            while mono_desc_promote and nums[mono_desc_promote[-1]] < nums[i]:
                results[mono_desc_promote.pop()] = nums[i] # these are also descending ordered because we check every nums[i]
            
            mono_desc_promote += temp 
            mono_desc.append(i)
        
        return results
            