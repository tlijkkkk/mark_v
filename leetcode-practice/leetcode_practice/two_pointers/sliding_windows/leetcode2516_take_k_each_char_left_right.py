from collections import Counter, defaultdict
from typing import Dict

class Solution:
    def take_k_each_char_left_right(self, s: str, k: int) -> int:
        counter: Dict[str, int] = dict(Counter(s))
        dt_counter: Dict[str, int] = defaultdict(int)
        max_len = 0
        i = 0

        if k == 0:
            return 0

        if len(counter) < 3 or any( x < k for x in counter.values()):
            return -1

        for j in range(len(s)):
            dt_counter[s[j]] += 1

            while dt_counter[s[j]] > counter[s[j]] - k:
                dt_counter[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j - i + 1)
        
        return len(s) - max_len