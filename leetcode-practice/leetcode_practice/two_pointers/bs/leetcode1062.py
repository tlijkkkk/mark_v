from typing import Set


class Solution:
    def longestRepeatingSubString(self, s: str) -> int:
        low = 0
        high = len(s) - 1
        maxLen = 0

        def isRepeating(length: int) -> bool:
            ss: Set[str] = set()
            for i in range(0, len(s) - length + 1):
                if s[i:i + length] in ss:
                    return True
                
                ss.add(s[i: i + length])
            return False

        while low <= high:
            mid = low + (high - low) // 2

            if isRepeating(mid):
                maxLen = max(maxLen, mid)
                low = mid + 1
            else:
                high = mid - 1

        return maxLen

    