from typing import List


class Solution:
    def longestCommonSubSeq(self, text1: str, text2: str) -> int:
        dp: List[int] = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            current: List[int] = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    current[j + 1] = dp[j] + 1
                else:
                    current[j + 1] = max(current[j], dp[j + 1])
        
            dp = current
        
        return max(dp)