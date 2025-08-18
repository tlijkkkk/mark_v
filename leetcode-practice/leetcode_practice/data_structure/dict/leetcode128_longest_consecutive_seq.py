from typing import List, Set


class Solution:
    def longest_consecutive_seq(self, nums: List[int]) -> int:
        num_set: Set[int] = set()

        for num in nums:
            num_set.add(num)

        longest = 0
        for num in num_set:
            if num + 1 not in num_set: # without this check won't achieve O(n) time complexity
                i = num
                count = 0
                while i in num_set:
                    i -= 1
                    count += 1
                longest = max(longest, count)
        
        return longest