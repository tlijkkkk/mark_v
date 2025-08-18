from typing import List

class Solution:
    def make_array_non_desc(self, nums: List[int]) -> int:
        mono_desc: List[int] = []

        for i in range(len(nums) - 1, -1, -1):
            while mono_desc and mono_desc[-1] < nums[i]:
                mono_desc.pop()
            
            mono_desc.append(nums[i])

        
        return len(mono_desc)
