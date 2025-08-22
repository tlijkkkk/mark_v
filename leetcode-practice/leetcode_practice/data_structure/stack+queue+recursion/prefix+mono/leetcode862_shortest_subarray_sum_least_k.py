from typing import List, Deque
from collections import deque

class Solution:
    def shortest_subarray_sum_least_k(self, nums: List[int], k: int) -> int:
        prefix_sum: List[int] = [0] * (len(nums) + 1)
        mono_asc: Deque[int] = deque()
        mono_asc.append((0, -1))
        shortest = float('inf')

        for j in range(len(nums)):
            prefix_sum[j + 1] = prefix_sum[j] + nums[j]
            
            while mono_asc and mono_asc[-1][0] > prefix_sum[j + 1]:
                mono_asc.pop()
            
            while mono_asc and prefix_sum[j + 1] - mono_asc[0][0] >= k:
                shortest = min(shortest, j - mono_asc[0][1])
                mono_asc.popleft()

            mono_asc.append((prefix_sum[j + 1], j))
        
        return shortest if shortest != float('inf') else -1

            







