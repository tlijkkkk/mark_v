from typing import List

class Solution:
    def next_greater_element_i(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_greater = {}
        stack = []
        ans = []
        for num in nums2:
            while stack and stack[-1] < num:
                num_greater[stack.pop()] = num
            stack.append(num)
            
        for num in nums1:
            ans.append(num_greater.get(num, -1))
        
        return ans