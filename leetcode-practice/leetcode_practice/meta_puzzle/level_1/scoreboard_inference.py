# You are spectating a programming contest with N competitors, each trying to independently solve the same set of programming problems. Each problem has a point value of either 1 or 2.

# On the scoreboard, you observe that the i-th competitor has attained a score of S[i], which is a positive integer equal to the sum of the point values of all the problems they have solved.

# The scoreboard does not display the number of problems in the contest, nor the specific point values of the problems. Using the information available, determine the minimum possible number of problems that could be in the contest.

# Constraints:
# - 1 ≤ N ≤ 500,000
# - 1 ≤ S[i] ≤ 1,000,000,000

from typing import List

def get_min_problem_count(N: int, S: List[int]) -> int:
    min_count = 0
    has_odd_score = any(score % 2 == 1 for score in S)
    
    max_score = max(S)
    if has_odd_score:
        min_count = max_score // 2 + 1
    else:
        min_count = max_score // 2
        
    return min_count


