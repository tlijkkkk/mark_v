from typing import List
from sortedcontainers import SortedList

class Solution:
    def contains_duplicate_iii(self, nums: List[int], index_diff: int, value_diff: int) -> bool:
        s_window = SortedList()
        i, j = 0, 0

        while j < len(nums):
            if j - i > index_diff:
                s_window.remove(nums[i])
                i += 1

            idx = s_window.bisect_left(nums[j] - value_diff)

            if idx < len(s_window) and abs(s_window[idx] - nums[j]) <= value_diff:
                return True
            
            s_window.add(nums[j])
            j += 1

        return False
