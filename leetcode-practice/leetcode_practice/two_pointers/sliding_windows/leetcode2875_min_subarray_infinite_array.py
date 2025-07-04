from typing import List

class Solution:
    def min_subarray_infinite_array(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        remaining = target % total_sum
        full_count = target // total_sum

        new_target = total_sum - remaining

        i = 0
        tmp_sum = 0
        shortest = float('inf')

        for j in range(len(nums)):
            tmp_sum += nums[j]

            while tmp_sum > remaining:
                tmp_sum -= 1
                i += 1

            if tmp_sum == remaining:
                shortest = min(shortest, j - i + 1)

        i = 0
        tmp_sum = 0
        longest = 0
        for j in range(len(nums)):
            tmp_sum += nums[j]

            while tmp_sum > new_target:
                tmp_sum -= nums[i]
                i += 1

            if tmp_sum == new_target:
                longest = max(longest, j - i + 1)
        
        if shortest == float('inf') and longest == 0:
            return -1

        result = min(shortest, len(nums) - longest) + len(nums) * full_count

        return result