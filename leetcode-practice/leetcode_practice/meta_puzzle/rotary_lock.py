# You're trying to open a lock. The lock has a wheel with integers from 1 to N arranged in a circle in order (with 1 and N adjacent). The wheel initially points to 1.

# It takes 1 second to rotate the wheel by 1 unit to an adjacent number in either direction (clockwise or counterclockwise). Selecting an integer takes no time once the wheel is pointing at it.

# The lock will open if you enter a certain code, which is a sequence of M integers. You must enter the code in order: the i-th number to enter is C[i].

# Determine the minimum number of seconds required to select all M of the code's integers in order.

# Constraints:
# - 3 ≤ N ≤ 50,000,000
# - 1 ≤ M ≤ 1,000
# - 1 ≤ C[i] ≤ N

from typing import List

def get_min_code_entry_time(N: int, M: int, C: List[int]) -> int:
  current = 1
  time_need = 0
  
  for code in C:
    time_need += min(abs(code - current), N - abs(code - current))
    current = code
  
  return time_need