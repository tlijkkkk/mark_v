from typing import Dict, List


class Solution:
    cache: Dict[str, List[int]] = {}

    def __init__(self, words: List[str]):
        for i in range(len(words)):
            self.cache[words[i]] = self.cache.get(words[i], []).append(i)

    def shortest_word_distance_ii(self, word1: str, word2: str):
        l1 = self.cache[word1]
        l2 = self.cache[word2]

        i = 0
        j = 0
        shortest_distance = float('inf')     
        while i < len(l1) and j < len(l2):
            shortest_distance = min(shortest_distance, abs(l1[i] - l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1

        return shortest_distance


