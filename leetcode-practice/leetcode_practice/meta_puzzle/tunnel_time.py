# There’s a circular train track with a circumference of C metres. Positions along the track are measured in metres, clockwise from its topmost point. For example, the topmost point is position 0, 1 metre clockwise along the track is position 1, and 1 metre counterclockwise along the track is position C−1.

# A train with negligible length runs clockwise along this track at a speed of 1 metre per second, starting from position 0. After C seconds go by, the train will have driven around the entire track and returned to position 0, at which point it will continue going around again, with this process repeated indefinitely.

# There are N tunnels covering sections of the track, the i-th of which begins at position Ai and ends at position Bi (and therefore has a length of Bi−Ai metres). No tunnel covers or touches position 0 (including at its endpoints), and no two tunnels intersect or touch one another (including at their endpoints). For example, if there's a tunnel spanning the interval of positions [1,4], there cannot be another tunnel spanning intervals [2,3] nor [4,5].

# The train’s tunnel time is the total number of seconds it has spent going through tunnels so far. Determine the total number of seconds which will go by before the train’s tunnel time becomes K.

# Constraints:
# 3 ≤ C ≤ 10^12
# 1 ≤ N ≤ 500000
# 1 ≤ Ai < Bi ≤ C−1
# 1 ≤ K ≤ 10^12

from typing import List

def get_seconds_elapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    tunnel_intervals = sorted(zip(A, B))  # sort by Ai
    total_tunnel_time = sum(b - a for a, b in tunnel_intervals)

    full_cycles = K // total_tunnel_time
    remaining = K % total_tunnel_time
    total_time = full_cycles * C

    if remaining == 0:
        return total_time - C + tunnel_intervals[-1][1]

    # Simulate inside one cycle until remaining tunnel time is reached
    for a, b in tunnel_intervals:
        length = b - a
        if remaining <= length:
            return total_time + a + remaining
        remaining -= length

    # This should not happen under valid constraints
    raise RuntimeError("Tunnel time exhausted without satisfying K")