from typing import List


class Solution:
    def longest_sub_array_with_sum_k(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if (prefix_sum - k) in prefix_sum_dict:
                max_len = max(max_len, i - prefix_sum_dict[prefix_sum - k])

            prefix_sum_dict.setdefault(prefix_sum, i)

        return max_len

        

            
        