from typing import List

class Solution:
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        desc_mono_stk = []
        result = []
        for num in nums2:
            while desc_mono_stk and desc_mono_stk[-1] < num:
                dict[desc_mono_stk.pop()] = num
            desc_mono_stk.append(num)
            
        for num in nums1:
            result.append(dict.get(num, -1))
        
        return result