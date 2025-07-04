from typing import List

class Solution:
    def count_subarrays_max_element_least_k_times(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        result = 0

        i = 0

        for j in range(len(nums)):
            count += 1 if nums[j] == max_num else 0

            while count >= k:
                count -= 1 if nums[i] == max_num else 0
                i += 1

            result += i
        
        return result
            
