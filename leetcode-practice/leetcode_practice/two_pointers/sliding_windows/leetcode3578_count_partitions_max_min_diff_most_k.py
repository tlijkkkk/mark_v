from typing import List, Deque
from collections import deque

class Solution:
    def count_partitions_max_min_diff_most_k(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        prefix_sum = [0] + [1] + [0] * len(nums)
        mono_min: Deque[int] = deque()
        mono_max: Deque[int] = deque()
        dp = [1] + [0] * len(nums)
        i = 0

        for j in range(len(nums)):
            while mono_min and mono_min[-1] > nums[j]:
                mono_min.pop()
            mono_min.append(nums[j])
            
            while mono_max and mono_max[-1] < nums[j]:
                mono_max.pop()
            mono_max.append(nums[j])

            while mono_max[0] - mono_min[0] > k:
                if nums[i] == mono_max[0]:
                    mono_max.popleft()
                elif nums[i] == mono_min[0]:
                    mono_min.popleft()
                i += 1

            dp[j + 1] = (prefix_sum[j + 1] - prefix_sum[i]) % MOD
            prefix_sum[j + 2] = (prefix_sum[j + 1] + dp[j + 1]) % MOD

        return dp[-1]



                
