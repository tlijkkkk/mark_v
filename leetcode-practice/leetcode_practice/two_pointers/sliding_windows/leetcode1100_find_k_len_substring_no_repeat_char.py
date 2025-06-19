from typing import Dict


class Solution:
    def find_k_length_substring_no_repeated_chars(self, s: str, k: int) -> int:
        dt_repeat: Dict[str, int] = {}

        i = 0
        result = 0

        for j in range(len(s)):
            if s[j] in dt_repeat:
                while i < dt_repeat[s[j]] + 1:
                    dt_repeat.pop(s[i])
                    i += 1
            
            dt_repeat[s[j]] = j

            if j - i + 1 > k:
                dt_repeat.pop(s[i])
                i += 1
            
            if j - i + 1 == k:
                result += 1

        return result
