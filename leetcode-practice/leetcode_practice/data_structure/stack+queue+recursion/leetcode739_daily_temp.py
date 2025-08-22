from typing import List

class Solution:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        mono_asc: List[int] = []
        result: List[int] = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while mono_asc and temperatures[mono_asc[-1]] <= temperatures[i]:
                mono_asc.pop()
            mono_asc.append(i)
            if len(mono_asc) > 1:
                result[i] = mono_asc[-2] - mono_asc[-1]

        return result

