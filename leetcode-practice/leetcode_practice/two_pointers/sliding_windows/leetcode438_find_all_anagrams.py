from typing import List, Dict
from collections import defaultdict, Counter

class Solution:
    def find_all_anagrams(self, s: str, p: str) -> List[int]:
        dt_char_count: Dict[str, int] = dict(Counter(p))
        result = []
        i = 0

        dt_tmp: Dict[str, int] = defaultdict(int)
        for j in range(len(s)):
            if s[j] in dt_char_count: 
                dt_tmp[s[j]] += 1
                
                while dt_tmp[s[j]] > dt_char_count[s[j]]:
                    dt_tmp[s[i]] -= 1
                    i += 1

                if dt_tmp == dt_char_count:
                    result.append(i)
            else:
                dt_tmp.clear()
                i = j + 1

        return result