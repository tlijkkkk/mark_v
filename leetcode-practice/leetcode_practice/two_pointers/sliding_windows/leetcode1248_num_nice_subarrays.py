from typing import List

class Solution:
    def num_nice_subarrays(self, nums: List[int], k: int) -> int:
        count = 0
        result = 0
        prefix_even_count = 0
        i = 0

        for j in range(len(nums)):
            if nums[j] % 2:
                count += 1
            
            while i < j and (not nums[i] % 2 or count > k):
                if nums[i] % 2:
                    prefix_even_count = 0
                    count -= 1
                else:
                    prefix_even_count += 1
                i += 1
            
            if count == k:
                result += 1 + prefix_even_count

        return result
            



    