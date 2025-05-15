from typing import List
from collections import deque


class Solution:
    def next_greater_element_iv(self, nums: List[int]) -> List[int]:
        mono_decrease_seen = []
        mono_decrease_first_greater = []
        results = [-1] * len(nums)

        for i in range(len(nums)):
            promotes = deque()
            while mono_decrease_seen and nums[mono_decrease_seen[-1]] < nums[i]:
                promotes.appendleft(mono_decrease_seen.pop()) # these are decending ordered indices that value less then current number, so they are the first batch of greaters that need to be promoted to the next
             
            while mono_decrease_first_greater and nums[mono_decrease_first_greater[-1]] < nums[i]:
                results[mono_decrease_first_greater.pop()] = nums[i] # these are also decending ordered because we check every nums[i]
            
            mono_decrease_first_greater += promotes 
            mono_decrease_seen.append(i)
        
        return results
            