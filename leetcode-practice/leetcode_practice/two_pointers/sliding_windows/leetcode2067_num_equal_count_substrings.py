from typing import Dict
from collections import defaultdict

class Solution:
    def num_equal_count_substrings(self, s: str, count: int) -> int:
        if count > len(s):
            return 0
        
        max_unique_count = len(set(s))
        result = 0

        for k in range(1, max_unique_count + 1):
            dt_unique_count: Dict[str, int] = defaultdict(int)
            dt_promo: Dict[str, int] = defaultdict(int)
            i = 0
            for j in range(len(s)):
                dt_unique_count[s[j]] += 1
                if dt_unique_count[s[j]] == count:
                    dt_promo[s[j]] = 1

                while j - i + 1 > k * count:
                    if dt_unique_count[s[i]] == count:
                        dt_promo.pop(s[i])
                    dt_unique_count[s[i]] -= 1
                    if dt_unique_count[s[i]] == 0:
                        dt_unique_count.pop(s[i])
                    i += 1
                
                if j - i + 1 == k * count and len(dt_promo) == k:
                    result += 1
        return result
        

            