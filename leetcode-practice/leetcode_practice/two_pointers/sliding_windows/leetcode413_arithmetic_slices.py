from typing import List
import math

class Solution:
    def count_arithmetic_slices(self, nums: List[int]) -> int:
        result = 0
        i, j = 0, 1

        while j < len(nums):
            if nums[j] - nums[j - 1] != nums[i + 1] - nums[i]:
                i = j - 1
            
            if j - i + 1 >= 3:
                result += j - i + 1 - 2

            j += 1

        return result
