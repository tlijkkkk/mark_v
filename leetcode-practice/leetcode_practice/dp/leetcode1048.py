from typing import List


class Solution:
    def longest_str_chain(self, words: List[str]) -> int:
        def is_predecessor(word1: str, word2: str):
            if len(word2) - len(word1) != 1:
                return False
            i = 0
            j = 0
            diff_count = 0
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
                else:
                    i += 1
                j += 1

            return True

        dp = [1] * len(words)
        sorted_words = sorted(words, key=lambda x: len(x))

        for i in range(len(sorted_words)):
            for j in range(i):
                if is_predecessor(sorted_words[j], sorted_words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)