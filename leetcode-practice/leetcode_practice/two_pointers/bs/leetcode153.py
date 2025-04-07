from typing import List


class Solution:
    def find_min_in_rotated_sorted_array(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j - 1:
            mid = i + (j - i) // 2
            if nums[mid] <= nums[j]:
                j = mid
            else:
                i = mid
        
        return min(nums[i], nums[j])
