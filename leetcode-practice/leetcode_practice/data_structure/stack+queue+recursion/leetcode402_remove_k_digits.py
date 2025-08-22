from typing import List, Deque
from collections import deque

class Solution:
    def remove_k_digits(self, num: str, k: int) -> str:
        mono_asc: Deque[int] = deque()
        count = 0

        for digit in num:
            while mono_asc and mono_asc[-1] > digit and count < k:
                mono_asc.pop()
                count += 1
            mono_asc.append(digit)
        
        while count < k:
            mono_asc.pop()
            count += 1

        if not mono_asc:
            return '0'

        while len(mono_asc) > 1 and mono_asc[0] == '0':
            mono_asc.popleft()

        return "".join(mono_asc)