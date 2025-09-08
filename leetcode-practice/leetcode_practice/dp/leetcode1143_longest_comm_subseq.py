from typing import List


class Solution:
    def longest_common_sub_seq(self, text1: str, text2: str) -> int:
        dp: List[int] = [0] * (len(s) + 1)
        result = 0

        for i in range(len(s)):
            current: List[int] = [0] * (len(s) + 1)
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    if i != j:
                        current[len(s) - j] = dp[len(s) - j - 1] + 2
                    else:
                        current[len(s) - j] = dp[len(s) - j - 1] + 1
                else:
                    current[len(s) - j] = max(dp[len(s) - j], current[len(s) - j - 1])
            result = max(result, max(current))
            dp = current

        return result