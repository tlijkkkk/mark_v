from typing import List, Dict
from collections import defaultdict

class Solution:
    def count_complete_subarrays(self, nums: List[int]) -> int:
        all_unique_count = len(set(nums))
        dt_unique_count: Dict[int, int] = defaultdict(int)
        result = 0

        i = 0
        for j in range(len(nums)):
            dt_unique_count[nums[j]] += 1

            while len(dt_unique_count) == all_unique_count:
                dt_unique_count[nums[i]] -= 1
                if dt_unique_count[nums[i]] == 0:
                    dt_unique_count.pop(nums[i])
                i += 1
            
            result += i
        
        return result
