from typing import List

class Solution:
    def min_ops_convert_zero(self, nums: List[int]) -> int:
        mono_asc: List[int] = [0]
        count = 0

        for num in nums:
            while mono_asc and mono_asc[-1] >= num:
                mono_asc.pop()

            if mono_asc[-1] < num:
                count += 1
            mono_asc.append(num)
        
        return count

            

