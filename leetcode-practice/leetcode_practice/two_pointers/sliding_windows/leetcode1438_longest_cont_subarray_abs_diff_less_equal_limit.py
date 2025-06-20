from typing import List, Deque
from collections import deque

class Solution:
    def longest_cont_subarray_abs_diff_less_equal_limit(self, nums: List[int], limit: int) -> int:
        max_mono: Deque[int] = deque()  # store indices
        min_mono: Deque[int] = deque()
        i = 0
        longest = 0

        for j in range(len(nums)):
            # Maintain decreasing deque for max
            while max_mono and nums[max_mono[-1]] <= nums[j]:
                max_mono.pop()
            max_mono.append(j)

            # Maintain increasing deque for min
            while min_mono and nums[min_mono[-1]] >= nums[j]:
                min_mono.pop()
            min_mono.append(j)

            # Shrink window if diff exceeds limit
            while nums[max_mono[0]] - nums[min_mono[0]] > limit:
                if max_mono[0] == i:
                    max_mono.popleft()
                if min_mono[0] == i:
                    min_mono.popleft()
                i += 1

            longest = max(longest, j - i + 1)

        return longest