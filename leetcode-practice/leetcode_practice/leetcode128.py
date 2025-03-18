from typing import List, Set


class Solution:
    def longestConsecutiveSeq(self, nums: List[int]) -> int:
        ss: Set[int] = set()

        for num in nums:
            ss.add(num)

        maxLen = 0
        for num in ss:
            if num - 1 not in ss:
                i = num
                count = 0
                while i in ss:
                    i += 1
                    count += 1
                maxLen = max(maxLen, count)
        
        return maxLen