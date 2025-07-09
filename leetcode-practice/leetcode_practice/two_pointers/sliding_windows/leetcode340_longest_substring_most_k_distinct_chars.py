from typing import Dict

class Solution:
    def longest_substring_most_k_distinct_chars(self, s: str, k: int) -> str:
        dt_chat_idx: Dict[str, int] = {}
        i = 0
        longest = ""

        for j in range(len(s)):
            dt_chat_idx[s[j]] = j
            
            if len(dt_chat_idx) > k:
                remove_key, idx = min(dt_chat_idx.items(), key=lambda item: item[1])
                i = idx + 1
                dt_chat_idx.pop(remove_key)

            if j - i + 1 > len(longest):
                longest = s[i: j + 1]
            
        return longest

