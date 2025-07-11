from typing import List

class Solution:
    def get_equal_substring_within_budget(self, s: str, t: str, max_cost: int) -> int:
        cost: List[int] = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s)) ]
        max_len = 0
        cost_so_far = 0
        i = 0

        for j in range(len(cost)):
            cost_so_far += cost[j]

            if cost_so_far > max_cost:
                cost_so_far -= cost[i]
                i += 1 

            max_len = max(max_len, j - i + 1)
        
        return max_len


