from bisect import bisect_left, insort
from itertools import accumulate
from typing import List


class Solution:
    def max_sum_rectangle_no_larger_than_k(self, matrix: list[List[int]], k: int) -> int:
        def max_subarray_sum_no_larger_than_k(nums: List[int], k: int) -> int:
            max_sum = float("-inf")
            prefix_sum = 0
            sorted_prefix_sums = [0]

            for num in nums:
                prefix_sum += num
                target = prefix_sum - k
                closest_idx = bisect_left(sorted_prefix_sums, target)
                if closest_idx < len(sorted_prefix_sums):
                    max_sum = max(max_sum, prefix_sum - sorted_prefix_sums[closest_idx])
                insort(sorted_prefix_sums, prefix_sum)

            return max_sum
        
        rows, cols = len(matrix), len(matrix[0])
        max_sum_rec = float('-inf')

        for left in range(cols):
            projected_nums = [0] * rows
            for right in range(left, cols):
                for i in range(rows):
                    projected_nums[i] += matrix[i][right]
                max_sum_rec = max(max_sum_rec, max_subarray_sum_no_larger_than_k(projected_nums, k))
        
        return max_sum_rec if max_sum_rec != float('-inf') else 0
            




