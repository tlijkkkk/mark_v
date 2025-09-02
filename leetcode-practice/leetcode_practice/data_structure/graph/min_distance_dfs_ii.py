# Find the shortest path between single source S and multiple destinations E in 2D matrix M, 
# if M[i][j] = '#' it means a block. If no such path, return -1

# Possible solutions can be
# 1. Use DFS
# 2. Improve DFS with branch prune
# 3. (Best) Use BFS

from typing import List, Tuple


class Solution:
    # Use Top down style + branch prune approach to imporve efficiency
    def min_distance_dfs_ii(self, M: List[List[str]], S: Tuple[int]) -> int:
        rows, cols = len(M), len(M[0])
        min_dist = [float('inf')]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(S: Tuple[int], dist: int):
            i, j = S[0], S[1]

            if not (0 <= i < rows and 0 <= j < cols) or M[i][j] == '#' or visited[i][j]:
                return
            
            if dist >= min_dist[0]:
                return 
            
            visited[i][j] = True

            if M[i][j] == 'E':
                min_dist[0] = dist
                return

            dfs((i + 1, j), dist + 1)
            dfs((i - 1, j), dist + 1)
            dfs((i, j + 1), dist + 1)
            dfs((i, j - 1), dist + 1)

            visited[i][j] = False

        dfs(S=S, dist=0)
        return min_dist[0] if min_dist[0] != float('inf') else -1

# But this approach can lead to lots of recomputing because min_dist is a single value.
# It tells you when your branch is longer than the min path found so far, but it cannot tell you
# if your current move is worse then other path that led to the same cell. 