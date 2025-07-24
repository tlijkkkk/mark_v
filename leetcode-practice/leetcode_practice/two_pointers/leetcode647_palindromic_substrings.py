from typing import List

class Solution:
    def palindromic_substring(self, s: str) -> int:
        result: List[str] = []

        for j in range(len(s)):
            result.append(s[j])
            
            i = j - 1
            k = j
            while i >= 0 and k < len(s) and s[i] == s[k]:
                result.append(s[i: k + 1])
                i -= 1
                k += 1
            
            i = j - 1
            k = j + 1
            while i >= 0 and k < len(s) and s[i] == s[k]:
                result.append(s[i: k + 1])
                i -= 1
                k += 1

        return result


