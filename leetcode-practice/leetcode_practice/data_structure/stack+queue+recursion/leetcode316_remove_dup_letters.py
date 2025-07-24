from typing import Dict, List, Set


class Solution:
    def remove_duplicate_letters(self, s: str) -> str:
        dt_unique_idx: Dict[str, int] = {c : i for i, c in enumerate(s)}

        mono_asc: List[str] = []
        unique_seen: Set[str] = set()

        for i in range(len(s)):
            if s[i] in unique_seen:
                continue # Give up if has been seen before because the same char is already in the best position

            while mono_asc and mono_asc[-1] > s[i] and i < dt_unique_idx[mono_asc[-1]]:
                c = mono_asc.pop()
                unique_seen.remove(c)

            mono_asc.append(s[i])
            unique_seen.add(s[i])

        return "".join(mono_asc)


