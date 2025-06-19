from typing import List, Dict

class Solution:
    # Use sliding window approach 
    def binary_subarray_sum(self, nums: List[int], goal: int) -> int:
        i = 0
        sum_so_far = 0
        prefix_zero_count = 0
        result = 0

        for j in range(len(nums)):
            sum_so_far += nums[j]
        
            while i < j and (not nums[i] or sum_so_far > goal):
                if nums[i]:
                    prefix_zero_count = 0
                    sum_so_far -= nums[i]
                else:
                    prefix_zero_count += 1                
                i += 1
            
            if sum_so_far == goal:
                result += 1 + prefix_zero_count
        
        return result
    
    # Use prefix-sum + dictionary approach 
    def binary_subarray_sum(self, nums: List[int], goal: int) -> int:
        dt_prefix_sum_freq: Dict[int, int] = {}
        prefix_sum = 0
        result = 0

        for j in range(len(nums)):
            prefix_sum += nums[j]
            if prefix_sum == goal:
                result += 1

            if prefix_sum - goal in dt_prefix_sum_freq:
                result += dt_prefix_sum_freq[prefix_sum - goal]
            
            dt_prefix_sum_freq[prefix_sum] = dt_prefix_sum_freq.get(prefix_sum, 0) + 1
        
        return result