from typing import List


class Solution:
    def shortest_word_distance(self, words: List[str], word1: str, word2: str) -> int:
        shortest_len = float('inf')
        w1 = -1
        w2 = -1

        for i in range(len(words)):
            if words[i] == word1:
                w1 = i
            elif words[i] == word2:
                w2 = i
            
            if w1 != -1 and w2 != -1:
                shortest_len = min(shortest_len, abs(w1 - w2))
            
        return shortest_len