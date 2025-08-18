from typing import List

class Solution:
    def steps_make_array_non_desc(self, nums: List[int]) -> int:
        mono_desc: List[int] = []
        count = 0
        result = 0

        for i in range(len(nums) - 1, -1, -1):
            count = 0
            while mono_desc and mono_desc[-1][0] < nums[i]:
                count = max(count + 1, mono_desc[-1][1])
                mono_desc.pop()
            
            result = max(result, count)
            mono_desc.append((nums[i], count))

        return result