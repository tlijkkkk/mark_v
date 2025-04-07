from typing import List, Set


class Solution:
    def longest_consecutive_seq(self, nums: List[int]) -> int:
        num_set: Set[int] = set()

        for num in nums:
            num_set.add(num)

        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                i = num
                count = 0
                while i in num_set:
                    i += 1
                    count += 1
                max_len = max(max_len, count)
        
        return max_len