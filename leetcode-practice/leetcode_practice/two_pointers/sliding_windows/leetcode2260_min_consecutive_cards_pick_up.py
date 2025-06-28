from typing import List, Dict

class Solution:
    def min_consecutive_cards_pick_up(self, cards: List[int]) -> int:
        dt_seen: Dict[int, int] = {}

        i = 0
        result = float('inf')

        for j in range(len(cards)):
            if cards[j] in dt_seen:
                match_idx = dt_seen[cards[j]]
                result = min(result, j - match_idx + 1)

                while i <= match_idx:
                    dt_seen.pop(cards[i])
                    i += 1

            dt_seen[cards[j]] = j
        
        return result if result != float('inf') else -1



