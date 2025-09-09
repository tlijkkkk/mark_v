from typing import List, Set

class Solution:
    def partition_string(self, s: str) -> List[str]:
        tmp = ""
        seen: Set[str] = set()
        result: List[str] = []

        for c in s:
            tmp += c
            if tmp not in seen:
                seen.add(tmp)
                result.append(tmp)
                tmp = ""
        
        return result
            
