from typing import List


class Solution:
    def max_gap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_num = max(nums)
        min_num = min(nums)
        
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1)) # Use floor division // to make sure bucket size is smaller than the theoretical minimum (max - min) / (n - 1) otherwise if len(nums) is large the ceiling rounded extra value that put into each bucket may cause error result. Use max(1, xxx) for case of having duplicates in nums
        num_of_buckets = (max_num - min_num) // bucket_size + 1

        buckets: List[List[float]] = [None for _ in range(num_of_buckets)] # [[min, max]]

        for num in nums:
            index = (num - min_num) // bucket_size
            if buckets[index] is None:
                buckets[index] = [num, num]
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)
        
        result = 0
        pre_max = min_num

        for i in range(num_of_buckets):
            if buckets[i] is not None:
                result = max(result, buckets[i][0] - pre_max)
                pre_max = buckets[i][1]

        return result
