from typing import List

class Solution:
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stk = []
        result = []
        for num in nums2:
            while stk and stk[-1] < num:
                dict[stk.pop()] = num
            stk.append(num)
            
        for num in nums1:
            result.append(dict.get(num, -1))
        
        return result