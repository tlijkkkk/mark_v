from typing import List

class Solution:
    def binary_subarray_sum(self, nums: List[int], goal: int) -> int:
        i, j = 0, 0
        the_sum = 0
        result = 0
        prefix_zero = 0

        while j < len(nums):
            the_sum += nums[j]
            prefix_zero = 0
        
            while the_sum > goal:
                the_sum -= nums[i]
                i += 1
            
            while nums[i] == 0:
                prefix_zero += 1
                i += 1

            if the_sum == goal:
                result += j - i + 1
            j += 1

        return result