from typing import List, Dict
from collections import Counter


class Solution:
    def max_freq_element_performing_ops_i(self, nums: List[int], k: int, num_operations: int) -> int:
        bitmap_count: List[int] = [0] * (max(nums) + k + 1)

        for num in nums:
            bitmap_count[num] += 1

        prefix_sum: List[int] = [0] * (len(bitmap_count))

        for i in range(1, len(bitmap_count)):
            prefix_sum[i] = prefix_sum[i - 1] + bitmap_count[i]
        
        result = 0
        
        for i in range(len(bitmap_count) - k):
            left = max(0, i - k - 1)
            right = min(i + k, len(bitmap_count) - 1)

            possible_convert_count = prefix_sum[right] - prefix_sum[left] - bitmap_count[i] 

            if possible_convert_count > num_operations:
                result = max(result, bitmap_count[i] + num_operations)
            else:
                result = max(result, bitmap_count[i] + possible_convert_count)
        
        return result


