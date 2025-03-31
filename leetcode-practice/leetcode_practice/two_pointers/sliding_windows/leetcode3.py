class Solution:
    def longest_substring_without_repeating_characters(self, s: str) -> int:
        max_len = 0
        i = 0
        j = 0
        char_map = {}

        while j < len(s):
            if s[j] in char_map:
                if i <= char_map[s[j]]:
                    i = char_map[s[j]] + 1
                
            char_map[s[j]] = j    
            max_len = max(max_len, j - i + 1)
            j += 1
        
        return max_len