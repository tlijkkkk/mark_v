from typing import Dict
from collections import defaultdict


class Solution:
    def longest_substring_most_2_distinct_chars(self, s: str) -> int:
        dt_char_idx: Dict[str, int] = {}
        longest = 0
        i = 0

        for j in range(len(s)):
            dt_char_idx[s[j]] = j
            if len(dt_char_idx) > 2:
                del_idx = min(dt_char_idx.values())
                i = del_idx + 1
                dt_char_idx.pop(s[del_idx])

            longest = max(longest, j - i + 1)
        
        return longest
        


