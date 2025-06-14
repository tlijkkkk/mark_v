from typing import List
import math

class Solution:
    def count_arithmetic_slices(self, nums: List[int]) -> int:
        result = 0
        i, j = 0, 1

        while j < len(nums):
            if nums[j] - nums[j - 1] != nums[i + 1] - nums[i]:
                if j - i >= 3:
                    n = j - i - 3 + 1
                    result += sum(range(n, 0, -1))
                i = j - 1

            j += 1

        if j - i >= 3:
            n = j - i - 3 + 1
            result += sum(range(n, 0, -1))

        return result
