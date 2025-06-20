import math

# Unique sliding window that slides in the middle 
class Solution:
    def min_delete_string_balance(self, s: str) -> int:
        left_b_count = 0
        right_a_count = s.count('a')
        min_del = right_a_count

        for c in s:
            if c == 'a':
                right_a_count -= 1
            
            min_del = min(min_del, left_b_count + right_a_count)
            
            if c == 'b':
                left_b_count += 1

        return min_del
