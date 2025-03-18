from typing import List


class Solution:
    # Leetcode original title: Edit distance
    def minEditDistance(self, word1: str, word2: str) -> int:
        dp: List[int] = [i for i in range(len(word2) + 1)] # watch out this init state 
        
        for i in range(len(word1)):
            current: List[int] = [i + 1] + [0] * len(word2)
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    current[j + 1] = dp[j]
                else:
                    current[j + 1] = min(current[j], dp[j], dp[j + 1]) + 1
            dp = current

        return dp[-1]