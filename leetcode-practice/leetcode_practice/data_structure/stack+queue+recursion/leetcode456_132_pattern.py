from typing import List

class Solution:
    def find_132_pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        mono_desc: List[int] = []
        second = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            
            while mono_desc and mono_desc[-1] < nums[i]:
                second = mono_desc.pop()
            
            mono_desc.append(nums[i])
        
        return False

        