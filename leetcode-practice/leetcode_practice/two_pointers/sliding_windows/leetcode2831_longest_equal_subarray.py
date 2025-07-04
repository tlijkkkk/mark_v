from typing import List, Dict
from collections import defaultdict

class Solution:
    def longest_equal_subarray(self, nums: List[int], k: int) -> int:
        dt_unique_idx: Dict[int, int] = defaultdict(list)
        longest = 0

        for i, v in enumerate(nums):
            dt_unique_idx[v].append(i)

        for indices in dt_unique_idx.values():
            i = 0
            for j in range(len(indices)):
                while indices[j] - indices[i] + 1 - (j - i + 1) > k:
                    i += 1
                longest = max(longest, j - i + 1)
        
        return longest