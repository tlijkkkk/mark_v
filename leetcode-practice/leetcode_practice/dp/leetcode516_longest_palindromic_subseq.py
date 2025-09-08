from typing import List

class Solution:
    def longest_palindromic_subseq(self, s) -> int:
        dp: List[int] = [0] * len(s)

        for i in range(len(s)):
            current: List[int] = [0] * len(s)
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j]:
                    current[len(s) - j] = dp[len(s) - j - 1] + 1
                else:
                    current[len(s) - j] = max(dp[len(s) - j], current[len(s) - j - 1])

            dp = current

        return dp[-1] * 2
