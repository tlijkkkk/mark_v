from typing import Set


class Solution:
    def longest_repeating_substring(self, s: str) -> int:
        low = 0
        high = len(s) - 1
        max_len = 0

        def is_repeating(length: int) -> bool:
            ss: Set[str] = set()
            for i in range(0, len(s) - length + 1):
                if s[i : i + length] in ss:
                    return True
                
                ss.add(s[i : i + length])
            return False

        while low <= high:
            mid = low + (high - low) // 2

            if is_repeating(mid):
                max_len = max(max_len, mid)
                low = mid + 1
            else:
                high = mid - 1

        return max_len

