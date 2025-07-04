from typing import Dict
from collections import defaultdict

class Solution:
    def count_substrings_k_frequency_chars_i(self, s: str, k: int) -> int:
        dt_char_count: Dict[str, int] = defaultdict(int) 
        count = 0
        i = 0

        for j in range(len(s)):
            dt_char_count[s[j]] += 1
            while dt_char_count[s[j]] == k:
                dt_char_count[s[i]] -= 1
                if dt_char_count[s[i]] == 0:
                    dt_char_count.pop(s[i])
                i += 1
            count += i
        
        return count
