from typing import List, Tuple

class Solution:
    def sum_subarray_min(self, arr: List[int]) -> int:
        larger_count: List[int] = [0] * len(arr)

        mono_asc: List[Tuple] = []
        for i in range(len(arr)):
            while mono_asc and mono_asc[-1][0] > arr[i]:
                mono_asc.pop()

            nearest_smaller_idx = -1
            if mono_asc:
                nearest_smaller_idx = mono_asc[-1][1]
            
            larger_count[i] += i - nearest_smaller_idx
            mono_asc.append((arr[i], i))

        mono_desc: List[Tuple] = []
        for i in range(len(arr) - 1, -1, -1):
            while mono_desc and mono_desc[-1][0] > arr[i]:
                mono_desc.pop()

            nearest_smaller_idx = len(arr)
            if mono_desc:
                nearest_smaller_idx = mono_desc[-1][1]
            
            larger_count[i] *= nearest_smaller_idx - i
            mono_desc.append((arr[i], i))

        return sum(arr[i] * count for i, count in enumerate(larger_count)) % (10 ** 9 + 7)
        
