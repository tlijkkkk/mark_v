from typing import Dict
from collections import defaultdict

class Solution:
    def longest_substring_without_repeating_characters(self, s: str) -> int:
        dt_char_count: Dict[str, int] = defaultdict(int)
        longest = 0
        i = 0

        for j in range(len(s)):
            dt_char_count[s[j]] += 1 
            while dt_char_count[s[j]] >= 2:
                dt_char_count[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)
        
        return longest