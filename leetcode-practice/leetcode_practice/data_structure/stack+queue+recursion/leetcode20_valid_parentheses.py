from typing import List

class Solution:
    def valid_parentheses(self, s: str) -> bool:
        ss: List[str] = []
        for c in s:
            if c in "({[":
                ss.append(c)
            elif ss:
                if ss[-1] == '(' and c == ')':
                    ss.pop()
                elif ss[-1] == '{' and c == '}':
                    ss.pop()
                elif ss[-1] == '[' and c ==']':
                    ss.pop()
                else:
                    return False
            else:
                return False
        
        return not ss