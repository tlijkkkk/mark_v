from typing import List

class Solution:
    def max_freq_element_k_operations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        i = 0
        tmp_sum = 0
        longest = 0

        for j in range(len(sorted_nums)):
            tmp_sum += sorted_nums[j]

            while sorted_nums[j] * (j - i + 1) - tmp_sum > k:
                tmp_sum -= sorted_nums[i]
                i += 1

            longest = max(longest, j - i + 1)
        
        return longest
