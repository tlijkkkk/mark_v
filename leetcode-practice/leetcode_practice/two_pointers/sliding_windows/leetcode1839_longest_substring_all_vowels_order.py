from typing import List

class Solution: 
    def longest_substring_all_vowels_order(self, word: str) -> int:
        vowels: List[str] = ['a', 'e', 'i', 'o', 'u']
        longest = 0
        i = 0
        p = 0

        for j in range(len(word)):
            if i < j and p < len(vowels) - 1 and word[j] == vowels[p + 1]:
                p += 1
            elif word[j] != vowels[p]:
                p = 0
                i = j if word[j] == vowels[p] else j + 1

            if p == len(vowels) - 1:
                longest = max(longest, j - i + 1)

        return longest

            


