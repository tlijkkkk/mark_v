from typing import List, Dict
from collections import defaultdict

class Solution:
    def distinct_nums_each_subarray(self, nums: List[int], k: int) -> List[int]:
        dt_unique: Dict[int, int] = defaultdict(int) 
        i = 0
        result: List[int] = []

        for j in range(len(nums)):
            dt_unique[nums[j]] += 1

            while j - i + 1 > k:
                dt_unique[nums[i]] -= 1
                if dt_unique[nums[i]] == 0:
                    dt_unique.pop(nums[i])
                i += 1
            
            if j - i + 1 == k:
                result.append(len(dt_unique))
        
        return result
