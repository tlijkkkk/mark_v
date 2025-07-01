from typing import List

class Solution:
    def max_win_two_segments(self, prize_positions: List[int], k: int) -> int:
        if len(prize_positions) == 1:
            return 1
        
        def get_prefix_max(prize_pos: List[int]) -> List[int]:
            i = 0
            prefix_max = 0
            prefix_max_array: List[int] = []
            for j in range(len(prize_pos)):
                while abs(prize_pos[j] - prize_pos[i]) > k:
                    i += 1

                prefix_max = max(prefix_max, j - i + 1)
                prefix_max_array.append(prefix_max)
            return prefix_max_array
                

        seg1_prefix_max: List[int] = get_prefix_max(prize_positions)
        seg2_prefix_max: List[int] = list(reversed(get_prefix_max(list(reversed(prize_positions)))))

        return max([seg1_prefix_max[i - 1] + seg2_prefix_max[i] for i in range(1, len(prize_positions))])
        
