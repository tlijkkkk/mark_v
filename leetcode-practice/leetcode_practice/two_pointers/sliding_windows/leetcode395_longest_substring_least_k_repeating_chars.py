from typing import Dict, Set

class Solution:
    def longest_substring_least_k_repeating_chars(self, s: str, k: int) -> int:
        st_unique: Set[str] = set(s)
        
        longest = 0

        for current_unique_count in range(1, len(st_unique) + 1):
            dt_char_count: Dict[str, int] = {}
            i = 0
            for j in range(len(s)):
                dt_char_count[s[j]] = dt_char_count.get(s[j], 0) + 1
                while len(dt_char_count) > current_unique_count:
                    dt_char_count[s[i]] -= 1
                    if dt_char_count[s[i]] == 0:
                        dt_char_count.pop(s[i])
                    i += 1
                
                if min(dt_char_count.values()) >= k:
                    longest = max(longest, j - i + 1) 

        return longest

