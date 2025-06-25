from typing import Dict, List
from collections import Counter
import itertools
from dataclasses import dataclass

@dataclass
class Group:
    letter: str
    size: int

class Solution:
    def swap_longest_repeated_char_substring(self, text: str) -> int:
        longest = 0
        dt_char_freq: Dict[str, int] = dict(Counter(text))
        groups: List[Group] = [Group(c, len(list(group))) for c, group in itertools.groupby(text)]

        for i in range(len(groups)):
            len_candidate = groups[i].size
            if dt_char_freq[groups[i].letter] > groups[i].size:
                len_candidate += 1
                if i - 2 >= 0 and groups[i].letter == groups[i - 2].letter and groups[i - 1].size == 1:
                    len_candidate = min(dt_char_freq[groups[i].letter], len_candidate + groups[i - 2].size)
            longest = max(longest,  len_candidate)

        return longest





        
