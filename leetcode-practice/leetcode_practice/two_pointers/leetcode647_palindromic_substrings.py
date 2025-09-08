from typing import List

class Solution:
    def palindromic_substring(self, s: str) -> int:
        result = 0

        for k in range(len(s)):
            result += 1
            
            i = k - 1
            j = k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1
            
            i = k - 1
            j = k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1

        return result


