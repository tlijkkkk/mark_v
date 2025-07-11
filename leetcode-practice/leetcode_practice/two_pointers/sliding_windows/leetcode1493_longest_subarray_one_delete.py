from typing import List

class Solution:
    def longest_subarray_one_delete(self, nums: List[int]) -> int:
        longest = 0
        zero_count = 0
        i = 0

        for j in range(len(nums)):
            zero_count += 1 if nums[j] == 0 else 0
            while zero_count > 1:
                zero_count -= 1 if nums[i] == 0 else 0
                i += 1
                
            longest = max(longest, j - i + 1)

        return longest - 1

