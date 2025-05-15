# There's a stack of N inflatable discs, with the i-th disc from the top having an initial radius of Ri inches. The stack is considered unstable if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be stable, each disc must have a strictly smaller radius than that of the disc directly under it.

# As long as the stack is unstable, you can repeatedly choose a disc and perform one of the following operations:

# Inflate the disc, increasing its radius by 1 inch. This operation takes A seconds and may be performed on discs of any radius (even those that exceed 10^9 inches).
# Deflate the disc, decreasing its radius by 1 inch. This operation takes B seconds and may only be performed if the resulting radius is a positive integer number of inches (that is, if the disc has a radius of at least 2" before being deflated).
# Determine the minimum number of seconds needed in order to make the stack stable.

# Constraints:
# 1 ≤ N ≤ 50
# 1 ≤ Ri ≤ 1,000,000,000
# 1 ≤ A, B ≤ 100

from typing import List


def get_min_seconds_required(N: int, R: List[int], A: int, B: int) -> int:
    R = [r - i for i, r in enumerate(R)] # R becomes the deviations from the mininum values that keeps the asec ordered list 

    ## Get Key Radii
    key_radii = {max(1, r) for r in R} # If below ths mininum value then it needs to inflat 
    key_radii = list(key_radii)
    key_radii.sort()
    
    cost_for_radius = [0] * len(key_radii)
    for r in R:
        for i, key_radius in enumerate(key_radii):
            delta = key_radius - r
            cost = 0
                    
            if delta > 0:
                cost = delta * A
            else:
                cost = -delta * B
                    
            if i == 0:
                cost_for_radius[0] += cost
            else:
                cost_for_radius[i] = min(cost_for_radius[i-1], cost_for_radius[i] + cost)
            
    return cost_for_radius[-1]