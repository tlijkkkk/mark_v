# There's a stack of N inflatable discs, with the i-th disc from the top having an initial radius of R[i] inches.

# The stack is considered unstable if it includes at least one disc whose radius is greater than or equal to the disc directly under it. 
# In other words, for the stack to be stable, each disc must have a strictly smaller radius than the disc directly under it.

# As long as the stack is unstable, you can repeatedly choose any disc and deflate it to have a smaller radius. 
# The new radius must be:
# - A positive integer
# - Strictly smaller than the disc’s current radius

# Your task is to determine the minimum number of discs you need to deflate to make the stack stable. 
# If it's impossible to stabilize the stack, return -1.

# Constraints:
# - 1 ≤ N ≤ 50
# - 1 ≤ R[i] ≤ 1,000,000,000



from typing import List

def get_min_deflate_disc_count(N: int, R: List[int]) -> int:
    change_count = 0

    for i in range(N - 1, 0, -1):
        if R[i] <= i:
            return -1
        if R[i - 1] >= R[i]:
            R[i - 1] = R[i] - 1
            change_count += 1

    return change_count
        