from typing import Set

class Solution:
    def split_string_max_num_unique_substrings(self, s: str) -> int:
        max_so_far = 0
        n = len(s)
        unique: Set[str] = set()

        def dfs(start: int, level: int):
            nonlocal max_so_far
            for i in range(start, n):
                substring = s[start: i + 1]
                if substring in unique:
                    continue
                
                unique.add(substring)
                max_so_far = max(max_so_far, level)
                if level + len(s) - 1 - i > max_so_far:
                    dfs(i + 1, level + 1)
                
                unique.remove(substring)

        dfs(0, 0)
        return max_so_far + 1