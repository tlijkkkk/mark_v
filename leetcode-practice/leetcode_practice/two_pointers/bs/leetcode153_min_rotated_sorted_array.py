from typing import List


class Solution:
    def find_min_in_rotated_sorted_array(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] <= nums[j]:
                j = mid
            else:
                i = mid + 1
        
        return nums[i]
