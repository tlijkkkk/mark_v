from typing import List, Tuple, Dict
from collections import defaultdict

class Solution:
    def count_zero_request_servers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        sorted_logs: List[List[int]] = sorted(logs, key=lambda log: log[1]) # sort logs by time
        sorted_queries: List[Tuple] = sorted([(q, i) for i, q in enumerate(queries)]) #sort queries by time
        server_count: Dict[int, int] = defaultdict(int)
        result = [0] * len(sorted_queries)
        i, j = 0, 0

        for q_time, idx in sorted_queries:
            while j < len(sorted_logs) and sorted_logs[j][1] <= q_time:
                server_count[sorted_logs[j][0]] += 1
                j += 1

            while i < j and sorted_logs[i][1] < q_time - x:
                server_count[sorted_logs[i][0]] -= 1
                if server_count[sorted_logs[i][0]] == 0:
                    server_count.pop(sorted_logs[i][0])
                i += 1

            result[idx] = n - len(server_count)

        return result 
