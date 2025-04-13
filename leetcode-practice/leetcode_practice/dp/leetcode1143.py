from typing import List


class Solution:
    def longest_common_sub_seq(self, text1: str, text2: str) -> int:
        dp: List[int] = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            current_row: List[int] = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    current_row[j + 1] = dp[j] + 1
                else:
                    current_row[j + 1] = max(current_row[j], dp[j + 1])
        
            dp = current_row
        
        return max(dp)