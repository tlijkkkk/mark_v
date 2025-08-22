from typing import List

class Solution:
    def __init__(self):
        self.mono_desc: List[int] = []
        self.day = 0
        

    def next(self, price: int) -> int:
        self.day += 1
        while self.mono_desc and self.mono_desc[-1][0] <= price:
            self.mono_desc.pop()
        
        span = self.day - self.mono_desc[-1][1] if self.mono_desc else self.day
        self.mono_desc.append((price, self.day))
        return span