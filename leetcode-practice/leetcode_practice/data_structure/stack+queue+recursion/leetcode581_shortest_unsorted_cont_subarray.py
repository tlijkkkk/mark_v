from typing import List

class Solution:
    def shortest_unsorted_cont_subarray(self, nums: List[int]) -> int:
        mono_asc: List[int] = []
        left = len(nums) - 1
        right = 0

        for i in range(len(nums)):
            while mono_asc and nums[mono_asc[-1]] > nums[i]:
                left = min(left, mono_asc.pop())
            mono_asc.append(i)

        mono_asc.clear()
        for i in range(len(nums) - 1, -1, -1):
            while mono_asc and nums[mono_asc[-1]] < nums[i]:
                right = max(right, mono_asc.pop())
            mono_asc.append(i)

        return right - left + 1 if left < right else 0