from typing import List

class Solution:
    def min_operations_reduce_x_zero(self, nums: List[int], x: int) -> int:
        i = 0
        tmp_sum = 0
        total = sum(nums)
        longest = 0

        if x > total:
            return -1
        
        if x == total:
            return len(nums)

        for j in range(len(nums)):
            tmp_sum += nums[j]
            
            while tmp_sum > total - x:
                tmp_sum -= nums[i]
                i += 1

            if tmp_sum == total - x:
                longest = max(longest, j - i + 1)
        
        return len(nums) - longest if longest != 0 else -1