from typing import List

class Solution:
    def compare_strings_freq_smallest_char(self, queries: List[str], words: List[str]) -> List[int]:
        def smallest_char_count(s: str) -> int:
            min_so_far = s[0]
            count = 0
            for c in s:
                if c < min_so_far:
                    min_so_far = c
                    count = 1
                elif c == min_so_far:
                    count += 1
            return count

        result: List[int] = []
        queriesFreq: List[int] = map(smallest_char_count, queries)
        wordsFreq: List[int] = map(smallest_char_count, words)

        for qf in queriesFreq:
            count = 0
            for wf in wordsFreq:
                if qf < wf:
                    count += 1
            result.append(count)
            
        return result
