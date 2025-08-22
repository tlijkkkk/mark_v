from typing import List

class Solution:
    def max_range_max(self, nums: List[int]) -> List[int]:
        result: List[int] = [0] * len(nums)
        
        mono_desc: List[int] = []
        for i in range(len(nums)):
            while mono_desc and nums[mono_desc[-1]] < nums[i]:
                mono_desc.pop()
            result[i] += i - mono_desc[-1] if mono_desc else i + 1
            mono_desc.append(i)

        mono_asc: List[int] = []
        for i in range(len(nums) - 1, -1, -1):
            while mono_asc and nums[mono_asc[-1]] < nums[i]:
                mono_asc.pop()
            result[i] += mono_asc[-1] - i if mono_asc else len(nums) - i
            result[i] -= 1
            mono_asc.append(i)

        return result
