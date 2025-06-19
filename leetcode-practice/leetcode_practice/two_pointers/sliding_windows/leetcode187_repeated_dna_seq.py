from typing import List, Dict

class Solution:
    def repeated_dna_seq(self, s: str) -> List[str]:
        dt_repeat: Dict[str, bool] = {}
        i = 0

        for j in range(9, len(s)):
            dt_repeat[s[i: j + 1]] = True if s[i: j + 1] in dt_repeat else False
            i += 1
        
        return [key for key in dt_repeat if dt_repeat[key]]