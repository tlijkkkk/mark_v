# You are the manager of a mail room which is frequently subject to theft. A period of N days is about to occur, such that on the i-th day, the following sequence of events will occur in order:

# A package with a value of V[i] dollars will get delivered to the mail room (unless V[i] = 0, in which case no package will get delivered).

# You can choose to pay C dollars to enter the mail room and collect all of the packages there (removing them from the room), and then leave the room.

# With probability S, all packages currently in the mail room will get stolen (and therefore removed from the room).

# Note that you're aware of the delivery schedule V[1..N], but can only observe the state of the mail room when you choose to enter it, meaning that you won't immediately be aware of whether or not packages were stolen at the end of any given day.

# Your profit after the Nth day will be equal to the total value of all packages which you collected up to that point, minus the total amount of money you spent on entering the mail room.

# Please determine the maximum expected profit you can achieve (in dollars).

# Note: Your return value must have an absolute or relative error of at most 10^-6 to be considered correct.

# Constraints:
# 1 <= N <= 4000
# 0 <= V[i] <= 1000
# 1 <= C <= 1000
# 0.0 <= S <= 1.0

from typing import List

def get_max_expected_profit(N: int, V: List[int], C: int, S: float) -> float:
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        stashed = V[i - 1]
        power = 1

        for j in range(i - 1, -1, -1):
            dp[i] = max(dp[i], dp[j] + stashed - C)
            if j > 0:
                power *= (1 - S)
                stashed += V[j - 1] * power
    return max(dp)