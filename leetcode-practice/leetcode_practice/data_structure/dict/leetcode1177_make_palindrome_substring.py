from typing import List, Dict
from collections import Counter

class Solution:
    def make_palindrome_substring(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix_count_mask: List[int] = [0] * (len(s) + 1)
        result = []

        for i in range(len(s)):
            prefix_count_mask[i + 1] = prefix_count_mask[i] ^ (1 << (ord(s[i]) - ord('a')))

        for i, j, k in queries:
            diff_mask = prefix_count_mask[j + 1] ^ prefix_count_mask[i]
            count = diff_mask.bit_count()
            result.append(count // 2 <= k)

        return result