import math
from typing import List


class Solution:
    def find_int_added_2_array_ii(self, nums1: List[int], nums2: List[int]) -> int:
        def is_valid(x: int) -> bool:
            i = j = removed = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] + x == nums2[j]:
                    j += 1
                else:
                    removed += 1
                i += 1
            removed += len(nums1) - i  # Account for any remaining elements
            return removed <= 2

        nums1.sort()
        nums2.sort()
        min_x = math.inf
        for i in range(min(3, len(nums1))):
            x = nums2[0] - nums1[i]
            if is_valid(x):
                min_x = min(min_x, x)
        return min_x
