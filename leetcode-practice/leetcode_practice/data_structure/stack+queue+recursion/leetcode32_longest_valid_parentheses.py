from typing import List

class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        ss_idx: List[int] = [-1] # init base is -1
        longest = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                ss_idx.append(i)
            else:
                ss_idx.pop()
                if not ss_idx: 
                    ss_idx.append(i) # base has pop, starting with ')' must be invalid, the position of this ')' becomes a new base
                else:
                    longest = max(longest, i - ss_idx[-1])
        
        return longest



