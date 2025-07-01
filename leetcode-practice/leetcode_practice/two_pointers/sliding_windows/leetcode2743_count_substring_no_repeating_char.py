from typing import Set

class Solution:
    def count_substring_no_repeating_char(self, s: str) -> int:
        s_unique: Set[str] = set()
        result = 0

        i = 0
        for j in range(len(s)):
            while s[j] in s_unique:
                s_unique.remove(s[i])
                i += 1
            
            s_unique.add(s[j])
            result += j - i + 1

        return result