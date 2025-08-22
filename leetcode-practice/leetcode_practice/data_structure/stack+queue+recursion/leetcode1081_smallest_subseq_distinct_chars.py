from typing import Dict, List, Set
from collections import Counter

class Solution:
    def smallest_subseq_distinct_chars(self, s: str) -> str:
        unseen_dist_char_count: Dict[str, int] = Counter(s)
        mono_asc: List[str] = []
        already_handled: Set = set()

        for c in s:
            unseen_dist_char_count[c] -= 1
            if unseen_dist_char_count[c] == 0:
                unseen_dist_char_count.pop(c)

            if c in already_handled:
                continue
            while mono_asc and mono_asc[-1] > c and mono_asc[-1] in unseen_dist_char_count:
                already_handled.remove(mono_asc[-1])
                mono_asc.pop()
                
            mono_asc.append(c)
            already_handled.add(c)

        return "".join(mono_asc)
                
            

        