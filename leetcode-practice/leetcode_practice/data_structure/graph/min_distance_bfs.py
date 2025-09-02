# Find the shortest path between single source S and multiple destinations E in 2D matrix M, 
# if M[i][j] = '#' it means a block. If no such path, return -1

# Possible solutions can be
# 1. Use DFS
# 2. Improve DFS with branch prune
# 3. (Best) Use BFS

# Why BFS is the best because BFS traverses all possible adjacent cells before moving further. 
# So BFS guarantees no watse of time 

from collections import deque
from typing import List, Tuple


class Solution:
    def min_distance_bfs(self, M: List[List[str]], S: Tuple[int]) -> int:
        rows, cols = len(M), len(M[0])
        queue = deque()
        queue.append((S[0], S[1], 0))
        visited = {S}

        while queue:
            i, j, dist = queue.popleft()
            if M[i][j] == 'E':
                return dist

            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = delta_i + i, delta_j + j
                if (0 <= next_i < rows and 0 <= next_j < cols and (next_i, next_j) not in visited 
                        and M[next_i][next_j] != '#'):
                    queue.append((next_i, next_j, dist + 1))
                    visited.add((next_i, next_j))
            
        return -1