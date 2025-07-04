from typing import List
from sortedcontainers import SortedList

class Solution:
    def count_subarrays_more_ones_than_zeros(self, nums: List[int]):
        sorted_prefix_sum: SortedList[int] = SortedList([0])
        trans_nums: List[int] = [1 if x == 1 else -1 for x in nums]
        prefix_sum = 0
        result = 0

        for num in trans_nums:
            prefix_sum += num

            # find where is the position of prefix_sum
            pos = sorted_prefix_sum.bisect_left(prefix_sum)
            result += pos
            result %= 10 ** 9 + 7

            sorted_prefix_sum.add(prefix_sum)
        return result