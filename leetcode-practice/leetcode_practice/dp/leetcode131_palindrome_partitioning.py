from typing import List
from functools import lru_cache


class Solution:
    def palindrome_partitioning(self, s: str) -> List[List[str]]:
        result = []

        @lru_cache(maxsize=None)
        def is_palindrome(i: int, j: int):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def do_partition(i: int, path: List[str]):
            if i == len(s):
                result.append(path[:])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    path.append(s[i : j + 1])
                    do_partition(j + 1, path)
                    path.pop()
        
        do_partition(0, [])

        return result