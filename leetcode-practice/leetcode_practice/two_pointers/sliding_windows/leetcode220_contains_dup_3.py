from typing import List
from sortedcontainers import SortedList

class Solution:
    def contains_duplicate_iii(self, nums: List[int], index_diff: int, value_diff: int) -> bool:
        sorted_window: SortedList[int] = SortedList()
        i = 0

        for j in range(len(nums)):
            while j - i > index_diff:
                sorted_window.remove(nums[i])
                i += 1
            
            idx = sorted_window.bisect_left(nums[j] - value_diff)

            if idx < len(sorted_window) and abs(nums[j] - sorted_window[idx]) <= value_diff:
                return True
            
            sorted_window.add(nums[j])

        return False




