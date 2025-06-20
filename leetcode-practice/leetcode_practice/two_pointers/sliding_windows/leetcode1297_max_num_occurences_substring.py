from typing import Dict
from collections import defaultdict

class Solution:
    def max_num_occurences_substring(self, s: str, max_letters: int, min_size: int, max_size: int) -> int:
        dt_unique_count: Dict[str, int] = defaultdict(int)
        i = 0
        dt_occur: Dict[str, int] = defaultdict(int)

        for j in range(len(s)):
            dt_unique_count[s[j]] += 1

            while len(dt_unique_count) > max_letters or j - i + 1 > max_size:
                dt_unique_count[s[i]] -= 1
                if dt_unique_count[s[i]] == 0:
                    dt_unique_count.pop(s[i]) # safe because we are not iterating the dict directly
                i += 1

            if j - i + 1 >= min_size:
                dt_occur[s[i: j + 1]] += 1
                if j - i + 1 > min_size:
                    dt_occur[s[j - min_size + 1: j + 1]] += 1

        return max(dt_occur.values(), default=0)

