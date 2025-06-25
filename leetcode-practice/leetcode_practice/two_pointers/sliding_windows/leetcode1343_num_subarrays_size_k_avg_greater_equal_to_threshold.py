from typing import List

class Solution:
    def num_subarrays_size_k_avg_greater_equal_threshold(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        i = 0
        min_sum = threshold * k
        sum_so_far = 0

        for j in range(len(arr)):
            sum_so_far += arr[j]

            if j - i + 1 > k:
                sum_so_far -= arr[i]
                i += 1
            
            if j - i + 1 == k:
                count += 1 if sum_so_far >= min_sum else 0

        return count