from typing import List, Dict

class Solution:
    def max_sum_distinct_subarrays_length_k(self, nums: List[int], k: int) -> int:
        dt_unique_idx: Dict[int, int] = {}
        i = 0
        result = 0
        tmp_sum = 0

        for j in range(len(nums)):
            tmp_sum += nums[j]
            if nums[j] in dt_unique_idx:
                match_idx = dt_unique_idx[nums[j]]
                while i <= match_idx:
                    tmp_sum -= nums[i]
                    dt_unique_idx.pop(nums[i])
                    i += 1
            
            dt_unique_idx[nums[j]] = j

            while j - i + 1 > k:
                tmp_sum -= nums[i]
                dt_unique_idx.pop(nums[i])
                i += 1
            
            if j - i + 1 == k:
                result = max(result, tmp_sum)

        return result


