from typing import List

class Solution:
    def max_subarray_min_product(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix_sum: List[int] = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        left: List[int] = [0] * n
        right: List[int] = [0] * n
        mono_asc_left: List[int] = []
        mono_desc_right: List[int] = []

        for i in range(n):
            while mono_asc_left and nums[mono_asc_left[-1]] >= nums[i]:
                mono_asc_left.pop()
            left[i] = mono_asc_left[-1] if mono_asc_left else -1
            mono_asc_left.append(i)

        for i in range(n - 1, -1, -1):
            while mono_desc_right and nums[mono_desc_right[-1]] >= nums[i]:
                mono_desc_right.pop()
            right[i] = mono_desc_right[-1] if mono_desc_right else n

            mono_desc_right.append(i)

        result = 0
        for i in range(n):
            result = max(result, nums[i] * (prefix_sum[right[i]] - prefix_sum[left[i]] + 1)) # prefix_sum's index mapping needs to + 1 

        return result % MOD
        
        

