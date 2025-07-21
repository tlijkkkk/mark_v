from typing import List


class Solution:
    def sum_subarray_ranges(self, nums: List[int]) -> int:
        mono_increasing_stack = []
        mono_decreasing_stack = []
        sum_range_min = 0
        sum_range_max = 0
        for i in range(len(nums) + 1):
            while mono_increasing_stack and (i == len(nums) or nums[mono_increasing_stack[-1]] > nums[i]):
                target_idx = mono_increasing_stack.pop()
                left_idx = -1 if not mono_increasing_stack else mono_increasing_stack[-1] 
                right_idx = i
                sum_range_min += nums[target_idx] * (target_idx - left_idx) * (right_idx - target_idx)
            mono_increasing_stack.append(i)
        for i in range(len(nums) + 1):
            while mono_decreasing_stack and (i == len(nums) or nums[mono_decreasing_stack[-1]] < nums[i]):
                target_idx = mono_decreasing_stack.pop()
                left_idx = -1 if not mono_decreasing_stack else mono_decreasing_stack[-1]
                right_idx = i
                sum_range_max += nums[target_idx] * (target_idx - left_idx) * (right_idx - target_idx)
            mono_decreasing_stack.append(i)
        
        return sum_range_max - sum_range_min
            
            