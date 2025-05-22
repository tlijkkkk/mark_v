from typing import List


class Solution:
    def subarray_sum_equals_k(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1} # prefix-sum needs to put dummy head for counting and length measure 
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

        return count
    