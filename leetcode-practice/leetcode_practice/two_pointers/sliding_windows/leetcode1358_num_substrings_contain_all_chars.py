from typing import Set, Dict
from collections import defaultdict

class Solution:
    def num_substrings_containing_all_chars(self, s: str) -> int:
        unique_count: Dict[str, int] = defaultdict(int)
        count = 0
        i = 0

        for j in range(len(s)):
            unique_count[s[j]] += 1

            while len(unique_count) == 3:
                unique_count[s[i]] -= 1
                if unique_count[s[i]] == 0:
                    unique_count.pop(s[i])
                i += 1
            
            count += i 
        
        return count

