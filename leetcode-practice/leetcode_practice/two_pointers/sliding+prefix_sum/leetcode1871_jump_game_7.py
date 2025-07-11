from typing import List

class Solution:
    def jump_game_vii(self, s: str, min_jump: int, max_jump: int) -> bool:
        if s[-1] == '1':
            return False
        
        reachable: List[bool] = [True] + [False] * (len(s) - 1)
        true_sum = 0

        for i in range(1, len(s)):
            if i - min_jump >= 0:
                true_sum += reachable[i - min_jump]
            
            if i - max_jump > 0:
                true_sum -= reachable[i - max_jump - 1]

            if s[i] == '0' or true_sum > 0: # if s[i] is based on a window which has any reachable == true
                reachable[i] = True
        
        return reachable[-1]