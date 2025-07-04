from typing import List, Dict
from collections import defaultdict

class Solution:
    def max_sum_almost_unique_subarray(self, nums: List[int], m: int, k: int) -> int:
        dt_unique_count: Dict[int, int] = defaultdict(int)
        tmp_sum = 0
        result = 0

        i = 0
        for j in range(len(nums)):
            tmp_sum += nums[j]

            dt_unique_count[nums[j]] += 1

            while j - i + 1 > k:
                tmp_sum -= nums[i]
                dt_unique_count[nums[i]] -= 1
                if dt_unique_count[nums[i]] == 0:
                    dt_unique_count.pop(nums[i])
                i += 1
            
            if j - i + 1 == k and len(dt_unique_count) >= m:
                result = max(result, tmp_sum)
        
        return result
