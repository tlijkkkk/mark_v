from typing import Dict

class Solution:
    def longest_substring_without_repeating_characters(self, s: str) -> int:
        max_len = 0
        i = 0
        dt_char_count: Dict[str, int] = {}

        for j in range(len(s)):
            if s[j] in dt_char_count:
                if i <= dt_char_count[s[j]]:
                    i = dt_char_count[s[j]] + 1
                
            dt_char_count[s[j]] = j    
            max_len = max(max_len, j - i + 1)
        
        return max_len