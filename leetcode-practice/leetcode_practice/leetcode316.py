from typing import Dict, List, Set


class Solution:
    def remove_duplicate_letters(self, s: str) -> str:
        m: Dict[str, int] = {c : i for i, c in enumerate(s)}

        stk: List[str] = []
        uni_str_in_stk: Set[str] = set()

        for i in range(len(s)):
            if s[i] in uni_str_in_stk:
                continue # Give up if has been seen before because the same char is already in the best position

            while stk and s[i] < stk[-1] and i < m[stk[-1]]:
                c = stk.pop()
                uni_str_in_stk.remove(c)

            stk.append(s[i])
            uni_str_in_stk.add(s[i])

        return "".join(stk)


