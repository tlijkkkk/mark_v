from typing import Set

class Solution:
    def find_max_num_non_intersecting_substrings(self, word: str) -> int:
        max_num = 0

        char_open_idx: Dict[str, int] = {}

        for i in range(len(word)):
            if word[i] not in char_open_idx:
                char_open_idx[word[i]] = i
            elif i - char_open_idx[word[i]] + 1 >= 4:
                max_num += 1
                char_open_idx.clear()

        return max_num