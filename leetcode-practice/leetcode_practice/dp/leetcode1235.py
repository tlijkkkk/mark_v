from bisect import bisect_right
from typing import List


class Solution:
    def max_profit_job_scheduling(self, start_time: List[int], end_time: List[int], profit: List[int]) -> int:
        sorted_endtime_jobs = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])
        sorted_endtime = [job[1] for job in sorted_endtime_jobs]
        profit_dp = [sorted_endtime_jobs[0][2]] + [0] * (len(profit) - 1)

        for i in range(1, len(sorted_endtime_jobs)):
            j = bisect_right(sorted_endtime, sorted_endtime_jobs[i][0]) - 1
            if j == -1:
                profit_dp[i] = max(profit_dp[i], sorted_endtime_jobs[i][2])
            else:
                profit_dp[i] = max(profit_dp[i], profit_dp[j] + sorted_endtime_jobs[i][2])

            profit_dp[i] = max(profit_dp[i], profit_dp[i - 1])
            

        return profit_dp[-1]


        