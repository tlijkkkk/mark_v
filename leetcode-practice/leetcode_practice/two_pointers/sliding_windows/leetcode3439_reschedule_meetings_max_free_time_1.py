from typing import List

class Solution:
    def reschedule_meetings_max_free_time_i(self, event_time: int, k: int, start_time: List[int], end_time: List[int]) -> int:
        free_end_time = start_time + [event_time]
        free_start_time = [0] + end_time
        tmp_sum = 0
        i = 0
        result = 0

        for j in range(len(free_end_time)):
            tmp_sum += free_end_time[j] - free_start_time[j]

            while j - i + 1 > k + 1:
                tmp_sum -= free_end_time[i] - free_start_time[i]
                i += 1

            result = max(result, tmp_sum)
        
        return result
            