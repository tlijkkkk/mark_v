from typing import List


class Solution:
    def subarray_sums_divisible_k(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        remain_count = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remain = prefix_sum % k

            if remain < 0:
                remain += k

            if remain in remain_count:
                count += remain_count[remain]
                remain_count[remain] += 1
            else:
                remain_count[remain] = 1

        return count
