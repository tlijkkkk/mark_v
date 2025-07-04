from typing import List, Dict
from collections import defaultdict

class Solution:
    def length_longest_subarray_most_k_frequency(self, nums: List[int], k: int) -> int:
        dt_unique_count: Dict[int, int] = defaultdict(int)
        longest = 0

        i = 0

        for j in range(len(nums)):
            dt_unique_count[nums[j]] += 1

            while dt_unique_count[nums[j]] > k:
                dt_unique_count[nums[i]] -= 1
                
                if dt_unique_count[nums[i]] == 0:
                    dt_unique_count.pop(nums[i])
                i += 1

            longest = max(longest, j - i + 1)

        return longest

