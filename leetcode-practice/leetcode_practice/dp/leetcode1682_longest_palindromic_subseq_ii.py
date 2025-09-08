from typing import List, Tuple

class Solution:
    def longest_palindromic_subseq_ii(self, s: str) -> int:
        dp: List[Tuple[int, str]] = [(0, "")] * len(s)
        result = 0

        for i in range(len(s)):
            current: List[int] = [(0, "")] * len(s)
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j] and dp[len(s) - j - 1][1] != s[j]:
                    current[len(s) - j] = (dp[len(s) - j - 1][0] + 2, s[i])
                elif dp[len(s) - j][0] > current[len(s) - j - 1][0]:
                    current[len(s) - j] = dp[len(s) - j] 
                else:
                    current[len(s) - j] = current[len(s) - j - 1]

            result = max(result, max([c[0] for c in current]))
            dp = current

        return result
        
        