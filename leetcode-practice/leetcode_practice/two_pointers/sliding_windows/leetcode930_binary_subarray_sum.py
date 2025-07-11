from typing import List, Dict

class Solution:
    # Use sliding window approach 
    def binary_subarray_sum(self, nums: List[int], goal: int) -> int:
        tmp_sum = 0
        prefix_zero_count = 0
        result = 0
        i = 0

        for j in range(len(nums)):
            tmp_sum += nums[j]
        
            while i < j and (not nums[i] or tmp_sum > goal):
                if nums[i]:
                    prefix_zero_count = 0
                    tmp_sum -= nums[i]
                else:
                    prefix_zero_count += 1                
                i += 1
            
            if tmp_sum == goal:
                result += 1 + prefix_zero_count
        
        return result
    