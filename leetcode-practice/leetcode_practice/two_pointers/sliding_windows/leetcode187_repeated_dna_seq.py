from typing import List, Set

class Solution:
    def repeated_dna_seq(self, s: str) -> List[str]:
        s_repeat: Set[str] = set()
        result: Set[str] = set()
        i = 0

        for j in range(len(s)):
            while j - i + 1 > 10:
                i += 1
            
            if j - i + 1 == 10:
                dna = s[i: j + 1]
                if dna in s_repeat and dna not in result:
                    result.add(dna)
                else:
                    s_repeat.add(dna)
            
        return list(result)