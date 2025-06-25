from typing import List, Dict

class Solution:
    def min_sum_lengths_two_non_overlap_subarrays_target_sum(self, arr: List[int], target: int) -> int:
        dt_prefix_sum_idx: Dict[int, int] = {0: 0}
        prefix_sum = 0
        dp: List[int] = [float('inf')] * (len(arr) + 1)
        result = float('inf')
        min_len_so_far = float('inf')
        
        for j in range(len(arr)):
            prefix_sum += arr[j]
            dt_prefix_sum_idx[prefix_sum] = j + 1
            if prefix_sum - target in dt_prefix_sum_idx:
                i = dt_prefix_sum_idx[prefix_sum - target]
                min_len_so_far = min(min_len_so_far, j + 1 - i)
                result = min(result, dp[i] + j + 1 - i)
            dp[j + 1] = min_len_so_far

        return result if result != float('inf') else -1