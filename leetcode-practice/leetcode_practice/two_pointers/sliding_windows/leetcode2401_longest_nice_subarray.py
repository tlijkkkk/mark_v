from typing import List

class Solution:
    def longest_nice_subarray(self, nums: List[int]) -> int:
        bitmask = 0
        longest = 0

        i = 0
        for j in range(len(nums)):
            while bitmask & nums[j]:
                bitmask ^= nums[i]
                i += 1
            bitmask |= nums[j]
            
            longest = max(longest, j - i + 1)
        
        return longest