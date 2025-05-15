from typing import List


class Solution:
    def max_sum_circular_subarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sum_all = sum(nums)
        sum_for_max = nums[0]
        sum_for_min = nums[0]
        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            if sum_for_max + nums[i] < nums[i]:
                sum_for_max = nums[i]
            else:
                sum_for_max += nums[i]
            max_sum = max(max_sum, sum_for_max)
            
            if sum_for_min + nums[i] < nums[i]:
                sum_for_min += nums[i]
            else:
                sum_for_min = nums[i]
            min_sum = min(min_sum, sum_for_min)

        if min_sum == sum_all:
            return max_sum

        return max(max_sum, sum_all - min_sum)
