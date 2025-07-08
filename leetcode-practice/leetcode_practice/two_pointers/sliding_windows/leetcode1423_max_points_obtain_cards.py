from typing import List

class Solution:
    def max_points_obtain_cards(self, card_points: List[int], k: int) -> int:
        n = len(card_points)
        min_sum = float('inf')
        tmp_sum = 0

        i = 0

        for j in range(n):
            tmp_sum += card_points[j]

            while j - i + 1 > n - k:
                tmp_sum -= card_points[i]
                i += 1 
            
            if j - i + 1 == n - k:
                min_sum = min(min_sum, tmp_sum)
        
        return sum(card_points) - min_sum
