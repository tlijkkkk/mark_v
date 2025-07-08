from typing import Set

class Solution:
    def max_num_vowels_substring_k(self, s: str, k: int) -> int:
        vowels: Set[str] = {"a", "e", "i", "o", "u"}
        result = 0
        count = 0
        i = 0

        for j in range(len(s)):
            count += 1 if s[j] in vowels else 0

            while j - i + 1 > k:
                count -= 1 if s[i] in vowels else 0
                i += 1
            
            if j - i + 1 == k:
                result = max(result, count)
            
        return result
