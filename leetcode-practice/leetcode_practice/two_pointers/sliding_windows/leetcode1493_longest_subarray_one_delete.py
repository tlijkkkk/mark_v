from typing import List

class Solution:
    def longest_subarray_one_delete(self, nums: List[int]) -> int:
        deleted = False
        i = 0
        longest = 0
        tmp_sum = 0

        for j in range(len(nums)):
            tmp_sum += nums[j]
            if not nums[j]:
                while deleted:
                    if not nums[i]:
                        deleted = False
                    tmp_sum -= nums[i]
                    i += 1
                deleted = True
            longest = max(longest, tmp_sum)

        return longest if longest < len(nums) else longest - 1

