from typing import List, Dict

class Solution:
    def find_all_anagrams(self, s: str, p: str) -> List[int]:
        dt_char_count: Dict[str, int] = {}
        for c in p:
            dt_char_count[c] = dt_char_count.get(c, 0) + 1
        
        result = []
        i = 0

        dt_tmp: Dict[str, int] = {}
        for j in range(len(s)):
            if s[j] not in dt_char_count: 
                dt_tmp = {}
                i = j + 1
            else:
                dt_tmp[s[j]] = dt_tmp.get(s[j], 0) + 1
                
                while dt_tmp[s[j]] > dt_char_count[s[j]]:
                    dt_tmp[s[i]] -= 1
                    i += 1

            if dt_tmp == dt_char_count:
                result.append(i)
        
        return result