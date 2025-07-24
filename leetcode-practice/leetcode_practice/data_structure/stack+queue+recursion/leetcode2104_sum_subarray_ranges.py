from typing import List


class Solution:
    def sum_subarray_ranges(self, nums: List[int]) -> int:
        mono_asc: List[int] = []
        mono_desc: List[int] = []
        sum_range_min = 0
        sum_range_max = 0
        for i in range(len(nums) + 1):
            while mono_asc and (i == len(nums) or nums[mono_asc[-1]] > nums[i]):
                target_idx = mono_asc.pop()
                left_idx = -1 if not mono_asc else mono_asc[-1] 
                right_idx = i
                sum_range_min += nums[target_idx] * (target_idx - left_idx) * (right_idx - target_idx)
            mono_asc.append(i)
        for i in range(len(nums) + 1):
            while mono_desc and (i == len(nums) or nums[mono_desc[-1]] < nums[i]):
                target_idx = mono_desc.pop()
                left_idx = -1 if not mono_desc else mono_desc[-1]
                right_idx = i
                sum_range_max += nums[target_idx] * (target_idx - left_idx) * (right_idx - target_idx)
            mono_desc.append(i)
        
        return sum_range_max - sum_range_min
            
            