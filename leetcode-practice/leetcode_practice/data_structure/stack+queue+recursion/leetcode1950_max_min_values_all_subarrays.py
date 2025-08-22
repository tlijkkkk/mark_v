from typing import List

class Solution:
    def max_min_values_all_subarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mono_asc: List[int] = []

        mins_range: List[int] = [0] * n
        result: List[int] = [0] * n

        for i in range(n):
            while mono_asc and nums[mono_asc[-1]] >= nums[i]:
                mono_asc.pop()
            
            if not mono_asc:
                mins_range[i] = i + 1
            else:
                mins_range[i] = i - mono_asc[-1]
            mono_asc.append(i)

        mono_desc: List[int] = []
        for i in range(n -1, -1, -1):
            while mono_desc and nums[mono_desc[-1]] >= nums[i]:
                mono_desc.pop()
            
            if not mono_desc:
                mins_range[i] += n - i - 1 # -1 for removing the double count
            else:
                mins_range[i] += mono_desc[-1] -i - 1 # -1 for removing the double count
            mono_desc.append(i)

        for i in range(n):
            result[mins_range[i] - 1] = max(result[mins_range[i] - 1], nums[i])

        for i in range(n - 2, -1, -1):
            result[i] = max(result[i], result[i + 1])

        return result
