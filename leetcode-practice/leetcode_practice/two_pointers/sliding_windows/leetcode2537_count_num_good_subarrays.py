from typing import List, Dict
from collections import defaultdict

class Solution:
    def count_num_good_subarrays(self, nums: List[int], k: int) -> int:
        dt_unique_count: Dict[int, int] = defaultdict(int)
        result = 0
        tmp_pair_count = 0
        i = 0

        for j in range(len(nums)):
            tmp_pair_count += dt_unique_count[nums[j]]
            dt_unique_count[nums[j]] += 1
            
            while tmp_pair_count >= k:
                dt_unique_count[nums[i]] -= 1
                tmp_pair_count -= dt_unique_count[nums[i]]
                i += 1
            
            result += i
        
        return result