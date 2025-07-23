from typing import List, Dict

class Solution:
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict: Dict[int, int] = {}
        mono_desc: List[int] = []
        result: List[int] = []
        for num in nums2:
            while mono_desc and mono_desc[-1] < num:
                dict[mono_desc.pop()] = num
            mono_desc.append(num)
            
        for num in nums1:
            result.append(dict.get(num, -1))
        
        return result