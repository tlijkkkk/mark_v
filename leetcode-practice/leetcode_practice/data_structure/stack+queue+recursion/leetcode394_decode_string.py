from typing import List, Tuple

class Solution:
    def decode_string(self, s: str) -> str:
        ss: List[Tuple[str, int]] = []

        curr_str = ""
        num = 0
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                ss.append((curr_str, num))
                num = 0
                curr_str = ""
            elif c == ']':
                s, n = ss.pop()
                curr_str = s + curr_str * n
            else:
                curr_str += c

        return curr_str