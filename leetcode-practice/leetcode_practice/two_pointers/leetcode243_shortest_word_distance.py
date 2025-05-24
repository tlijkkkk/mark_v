from typing import List


class Solution:
    def shortest_word_distance(self, words: List[str], word1: str, word2: str) -> int:
        shortest_len = float('inf')
        w1_idx = -1
        w2_idx = -1

        for i in range(len(words)):
            if words[i] == word1:
                w1_idx = i
            elif words[i] == word2:
                w2_idx = i
            
            if w1_idx != -1 and w2_idx != -1:
                shortest_len = min(shortest_len, abs(w1_idx - w2_idx))
            
        return shortest_len