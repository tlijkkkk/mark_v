from typing import Dict


class Solution:
    def longest_substring_most_2_distinct_chars(self, s: str) -> int:
        dt_char_idx: Dict = {}
        longest = 0
        i = 0

        for j in range(len(s)):
            if s[j] not in dt_char_idx and len(dt_char_idx) >= 2:
                del_char = min(dt_char_idx, key=dt_char_idx.get)
                i = dt_char_idx[del_char] + 1
                dt_char_idx.pop(del_char)

            dt_char_idx[s[j]] = j
            longest = max(longest, j - i + 1)
        
        return longest
        


