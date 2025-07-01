from typing import List, Deque
from collections import deque

class Solution:
    def continuous_subarrays(self, nums: List[int]) -> int:
        mono_asc: Deque[int] = deque()
        mono_desc: Deque[int] = deque()

        i = 0
        result = 0

        for j in range(len(nums)):
            while mono_asc and mono_asc[-1] > nums[j]:
                mono_asc.pop()
            mono_asc.append(nums[j])

            while mono_desc and mono_desc[-1] < nums[j]:
                mono_desc.pop()
            mono_desc.append(nums[j])

            while nums[j] - mono_asc[0] > 2 or mono_desc[0] - nums[j] > 2:
                if nums[i] == mono_asc[0]:
                    mono_asc.popleft()
                if nums[i] == mono_desc[0]:
                    mono_desc.popleft()
                i += 1

            result += j - i + 1

        return result