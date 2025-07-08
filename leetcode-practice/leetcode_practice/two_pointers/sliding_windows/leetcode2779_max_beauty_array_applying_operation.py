from typing import List

class Solution:
    def max_beauty_array_applying_operation(self, nums: List[int], k: int) -> int:
        sorted_nums: List[int] = sorted(nums)
        max_len = 0
        i = 0

        for j in range(len(sorted_nums)):
            while sorted_nums[j] - sorted_nums[i] > 2 * k:
                i += 1
            max_len = max(max_len, j - i + 1)

        return max_len