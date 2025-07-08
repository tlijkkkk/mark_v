from typing import Dict
from collections import Counter

class Solution:
    def replace_substring_balanced_string(self, s: str) -> int:
        dt_count: Dict[str, int] = Counter(s)
        min_len = float('inf')

        i = 0

        if all(x <= (len(s) / 4) for x in dt_count.values()):
            return 0

        for j in range(len(s)):
            dt_count[s[j]] -= 1

            while all(x <= (len(s) / 4) for x in dt_count.values()):
                min_len = min(min_len, j - i + 1)
                dt_count[s[i]] += 1
                i += 1

        return min_len

