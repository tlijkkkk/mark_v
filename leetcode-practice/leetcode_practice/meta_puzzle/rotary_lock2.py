# You're trying to open a lock. The lock has two wheels, each of which has the integers from 1 to N arranged in a circle in order (with 1 and N adjacent). Both wheels initially point to 1.

# It takes 1 second to rotate a wheel by 1 unit to an adjacent number in either direction (clockwise or counterclockwise). Selecting an integer takes no time once a wheel is pointing at it.

# The lock will open if you enter a certain code — a sequence of M integers. You must enter the code in order: the i-th number to enter is C[i].  
# For each number in the code, you may choose to select it using either of the two wheels.

# Determine the minimum number of seconds required to enter the entire code using the two wheels optimally.

# Constraints:
# - 3 ≤ N ≤ 1,000,000,000
# - 1 ≤ M ≤ 3,000
# - 1 ≤ C[i] ≤ N

from typing import List

def get_min_code_entry_time_ii(N: int, M: int, C: List[int]) -> int:
    state_time = {(1,1): 0}

    for code in C:
        new_state_time = {}
        for left, right in state_time:
            # left
            time_left = state_time[(left, right)] + min(abs(code - left), N - abs(code - left))
            new_state_time[(code, right)] = min(new_state_time.get((code, right), float('inf')), time_left)

            # right
            time_right = state_time[(left, right)] + min(abs(code - right), N - abs(code - right))
            new_state_time[(left, code)] = min(new_state_time.get((left, code), float('inf')), time_right)
        state_time = new_state_time

    return min(state_time.values())
