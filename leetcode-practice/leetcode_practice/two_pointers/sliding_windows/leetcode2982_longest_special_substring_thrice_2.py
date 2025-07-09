from typing import Dict
from collections import defaultdict

class Solution:
    def longest_special_substring_thrice_ii(self, s: str) -> int:
        dt_special_count: Dict[str, int] = defaultdict(int)
        longest = -1
        
        left = 1
        right = len(s)

        while  left <= right:
            mid = left + (right - left) // 2
            
            found = False
            i = 0
            for j in range(len(s)):
                while s[j] != s[i] or j - i + 1 > mid:
                    i += 1
                
                if j - i + 1 == mid:
                    dt_special_count[s[i]] += 1

                    if dt_special_count[s[i]] == 3:
                        longest = mid
                        found = True
                        break
            if found:
                left = mid + 1
            else:
                right = mid - 1
            dt_special_count.clear()
        
        return longest
        

            