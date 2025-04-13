from typing import List


class Solution:
    def count_num_of_teams(self, rating: List[int]) -> int:
        counting_less_left: List[int] = [0] * len(rating)
        counting_larger_right: List[int] = [0] * len(rating)
        counting_larger_left: List[int] = [0] * len(rating)
        counting_less_right: List[int] = [0] * len(rating)
        count = 0

        for i in range(len(rating)):
            for j in range(i):
                if rating[i] > rating[j]:
                    counting_less_left[i] += 1
                elif rating[i] < rating[j]:
                    counting_larger_left[i] += 1
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    counting_larger_right[i] += 1
                elif rating[i] > rating[j]:
                    counting_less_right[i] += 1
                
            count += counting_less_left[i] * counting_larger_right[i] + counting_larger_left[i] *  counting_less_right[i]

        return count