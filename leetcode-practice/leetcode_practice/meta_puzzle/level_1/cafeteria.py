# A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. Social distancing guidelines require that every diner be seated such that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.

# There are currently M diners seated at the table, the i-th of whom is in seat S[i]. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

# Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.

# Please take care to write a solution which runs within the time limit.

# Constraints:
# 1 <= N <= 10^15
# 1 <= K <= N
# 1 <= M <= 500000
# M <= N
# 1 <= S[i] <= N

from typing import List

def get_max_addtional_diners_count(N: int, K: int, M: int, S: List[int]) -> int:
    count = 0
    SS = sorted(S)
    for i in range(len(SS)):
        if i == 0:
            count += (SS[i] - 1) // (K + 1)
        else:
            count += (SS[i] - SS[i - 1]) // (K + 1) - 1 

    count += (N - SS[-1]) // (K + 1)

    return count

