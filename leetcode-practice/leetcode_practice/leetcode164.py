from typing import List


class Solution:
    def max_gap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_num = max(nums)
        min_num = min(nums)
        
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1)) # Use floor division // to make sure bucket size is smaller than the theoretical minimum (max - min) / (n - 1) otherwise if len(nums) is large the ceiling rounded extra value that put into each bucket may cause error result. Use max(1, xxx) for case of having duplicates in nums
        num_of_buckets = (max_num - min_num) // bucket_size + 1

        buckets: List[List[float]] = [[float("-inf"), float("inf")] for _ in range(num_of_buckets)]

        for num in nums:
            index = (num - min_num) // bucket_size
            buckets[index][0] = max(buckets[index][0], num)
            buckets[index][1] = min(buckets[index][1], num)
        
        max_gap_len = 0
        pre_max = min_num

        for i in range(num_of_buckets):
            if buckets[i][0] == float("-inf"):
                continue
        
            max_gap_len = max(max_gap_len, buckets[i][1] - pre_max)
            pre_max = buckets[i][0]

        return max_gap_len
