from functools import cmp_to_key
from typing import List


class Solution:
    def largest_num(self, nums: List[int]) -> int:
        def compare(a: int, b: int) -> int:
            if str(a) + str(b) < str(b) + str(a):
                return -1
            elif str(a) + str(b) > str(b) + str(a):
                return 1
            else:
                return 0

        sorted_str_arr = list(map(str, sorted(nums, key=cmp_to_key(compare), reverse=True)))
        return "".join(sorted_str_arr) if sorted_str_arr[0] != "0" else "0"
