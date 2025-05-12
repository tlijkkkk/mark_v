class Solution:
    def max_repeat_substring(self, sequence: str, word: str) -> int:
        k = 0
        tmp = word
        if tmp in sequence:
            tmp += tmp
            k += 1
        
        return k