from typing import List

class Solution:
    def kth_smallest_subarray_sum(self, nums: List[int], k: int) -> int:
        
        def count_sum(target: int) -> int:
            tmp_sum = 0
            i = 0
            count = 0

            for j in range(len(nums)):
                tmp_sum += nums[j]
                while tmp_sum > target:
                    tmp_sum -= nums[i]
                    i += 1
                count += (j - i + 1)
            return count

        low, high = min(nums), sum(nums)

        while low < high:
            mid = low + (high - low) // 2
            if count_sum(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low