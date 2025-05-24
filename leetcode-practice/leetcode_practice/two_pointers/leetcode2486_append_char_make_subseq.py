class Solution:
    def append_char_2_str_make_subseq(self, s: str, t: str) -> int:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j

