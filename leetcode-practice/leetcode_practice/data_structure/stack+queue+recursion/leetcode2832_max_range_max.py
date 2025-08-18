from typing import List

class Solution:
    def max_range_max(self, nums: List[int]) -> List[int]:
        mono_desc: List[int] = []
        result: List[int] = [0] * len(nums)

        for i in range(len(nums)):
            while mono_desc and nums[mono_desc[-1]] < nums[i]:
                mono_desc.pop()
            result[i] += i - mono_desc[-1] if mono_desc else i + 1
            mono_desc.append(i)

        mono_desc.clear()
        for i in range(len(nums) - 1, -1, -1):
            while mono_desc and nums[mono_desc[-1]] < nums[i]:
                mono_desc.pop()
            result[i] += mono_desc[-1] - i if mono_desc else len(nums) - 1 - i + 1
            result[i] -= 1
            mono_desc.append(i)

        return result
