from typing import Dict, List, Set
from collections import Counter

class Solution:
    def min_deletion_make_char_freq_unique(self, s: str) -> int:
        char_freq: Dict[str, int] = dict(Counter(s))
        sorted_freq: List[int] = sorted(char_freq.values(), reverse=True)
        occupied: Set = set()
        count = 0

        for freq in sorted_freq:
            while freq > 0 and freq in occupied:
                count += 1
                freq -= 1
            occupied.add(freq)

        return count