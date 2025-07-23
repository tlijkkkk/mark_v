from typing import List

class Solution:
    def verify_preorder_sequence_bst(self, seq: List[int]) -> bool:
        mono_desc: List[int] = []
        lowest = float('inf')

        for num in seq:
            if lowest > num:
                return False

            while mono_desc and mono_desc[-1] < num:
                lowest = mono_desc.pop()

            mono_desc.append(num)

        return True