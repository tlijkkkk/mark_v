class Solution:
    def longest_repeating_char_replacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        char_count = {}
        max_repeat = 0
        max_len = 0

        while j < len(s):
            char_count[s[j]] = char_count.get(s[j], 0) + 1
            max_repeat = max(max_repeat, char_count[s[j]])

            while j - i + 1 - max_repeat > k: # shrink to k
                char_count[s[i]] -= 1 
                i += 1

            max_len = max(max_len, j - i + 1)

            j += 1

        return max_len

            
