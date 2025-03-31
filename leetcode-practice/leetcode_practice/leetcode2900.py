from typing import List


class Solution:
    def longest_unequal_adjacent_groups_sub_seq(self, words: List[str], groups: List[int]) -> List[str]:
        result: List[str] = [words[0]]
        i = 0
        j = 0

        while j < len(groups):
            if groups[j] != groups[i]:
                result.append(words[j])
                i = j
            j += 1
        

        return result
