from typing import List


class Solution:
    def countNumOfTeams(self, rating: List[int]) -> int:
        prefixCountingLess: List[int] = [0] * len(rating)
        prefixCountingLarger: List[int] = [0] * len(rating)
        count = 0

        for i in range(len(rating)):
            for j in range(len(rating)):
                if rating[i] < rating[j]:
                    prefixCountingLarger[i] += 1
                else:
                    prefixCountingLess[i] += 1
        
            count = prefixCountingLess[i] * prefixCountingLarger[i]

        return count