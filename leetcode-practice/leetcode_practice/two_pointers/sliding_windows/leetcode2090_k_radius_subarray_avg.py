from typing import List

class Solution:
    def k_radius_subarray_avg(self, nums: List[int], k: int) -> List[int]:
        result: List[int] = [-1] * len(nums)
        wind_size = 2 * k + 1
        tmp_sum = 0
        i = 0
        for j in range(len(nums)):
            tmp_sum += nums[j]

            while j - i + 1 > wind_size:
                tmp_sum -= nums[i]
                i += 1

            if j - i + 1 == wind_size:
                avg = tmp_sum // wind_size
                result[j - k] = avg

        return result    
                
                

            
