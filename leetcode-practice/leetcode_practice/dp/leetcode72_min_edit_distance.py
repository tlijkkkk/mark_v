from typing import List


class Solution:
    # Leetcode original title: Edit distance
    def min_edit_distance(self, word1: str, word2: str) -> int:
        dp: List[int] = [i for i in range(len(word2) + 1)]  # watch out this init state 
        
        for i in range(len(word1)):
            current_row: List[int] = [i + 1] + [0] * len(word2)
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    current_row[j + 1] = dp[j]
                else:
                    current_row[j + 1] = min(current_row[j], dp[j], dp[j + 1]) + 1
            dp = current_row

        return dp[-1]