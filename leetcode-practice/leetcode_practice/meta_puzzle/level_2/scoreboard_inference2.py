# You are spectating a programming contest with N competitors, each trying to independently solve the same set of programming problems. Each problem has a point value of either 1, 2, or 3.

# On the scoreboard, you observe that the i-th competitor has attained a score of S[i], which is a positive integer equal to the sum of the point values of all the problems they have solved.

# The scoreboard does not display the number of problems in the contest, nor their individual point values. Using the information available, you would like to determine the minimum possible number of problems that could be in the contest.

# Constraints:
# - 1 ≤ N ≤ 500,000
# - 1 ≤ S[i] ≤ 1,000,000,000

from typing import List

def get_min_problem_count(N: int, S: List[int]) -> int:
    max_score = max(S)
    has_one = any([score % 3 == 1 and score != max_score for score in S])
    has_two = any([score % 3 == 2 and score != max_score for score in S])
    has_exact_one = 1 in S
    max_score_multiple_3 = max((score for score in S if score % 3 == 0), default = 0)

    result = max_score // 3
    if max_score % 3 == 0 and (has_one or has_two):
        return result + 1
    
    if max_score % 3 == 1:
        if has_two and (has_exact_one or max_score_multiple_3 == result * 3):
            result += 1
        return result + 1

    if max_score % 3 == 2:
        if has_one:
            result += 1
        return result + 1
    
    return result