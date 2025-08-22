from typing import List

class Solution:
    def longest_well_performing_interval(self, hours: List[int]) -> int:
        prefix_sum: List[int] = [0] * (len(hours) + 1)

        for i in range(len(hours)):
            flag = 1 if hours[i] > 8 else -1
            prefix_sum[i + 1] = prefix_sum[i] + flag

        mono_desc: List[int] = []
        for i in range(len(hours) - 1, -1, -1): 
            if not mono_desc or prefix_sum[mono_desc[-1]] < prefix_sum[i + 1]:
                mono_desc.append(i + 1)
        
        longest = 0
        for i in range(len(prefix_sum)):
            if mono_desc and i == mono_desc[-1]:
                mono_desc.pop()
                continue
            while mono_desc and prefix_sum[i] < prefix_sum[mono_desc[-1]]:
                longest = max(longest, mono_desc[-1] - i)
                mono_desc.pop()

        return longest
